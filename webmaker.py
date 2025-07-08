import argparse
import os
import sys
import shutil
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"


def list_templates():
    """Return a list of available template names."""
    if not TEMPLATE_DIR.exists():
        return []
    return [p.name for p in TEMPLATE_DIR.iterdir() if p.is_dir()]


def copy_template(template_name: str, project_name: str):
    """Copy the specified template into a new project directory, replacing placeholders."""
    # Validate template
    src_dir = TEMPLATE_DIR / template_name
    if not src_dir.exists():
        print(f"Error: template '{template_name}' does not exist.")
        sys.exit(1)

    dest_dir = Path.cwd() / project_name
    if dest_dir.exists():
        print(f"Error: destination directory '{project_name}' already exists.")
        sys.exit(1)

    shutil.copytree(src_dir, dest_dir)

    # Perform placeholder substitution in text files
    for path in dest_dir.rglob("*"):
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                # Skip binary files (images, etc.)
                continue
            text = text.replace("{{project_name}}", project_name)
            path.write_text(text, encoding="utf-8")

    print(f"✅ Project '{project_name}' created using '{template_name}' template at {dest_dir}.")


def main():
    parser = argparse.ArgumentParser(description="web-maker: A simple website project generator.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list command
    list_parser = subparsers.add_parser("list", help="List available templates")

    # new command
    new_parser = subparsers.add_parser("new", help="Create a new project from a template")
    new_parser.add_argument("template", type=str, help="Template name")
    new_parser.add_argument("project_name", type=str, help="Name of the new project directory")

    args = parser.parse_args()

    if args.command == "list":
        templates = list_templates()
        if not templates:
            print("No templates available.")
        else:
            print("Available templates:")
            for t in templates:
                print(f" - {t}")
    elif args.command == "new":
        copy_template(args.template, args.project_name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()