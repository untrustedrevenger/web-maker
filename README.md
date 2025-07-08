# web-maker

**web-maker** is a versatile repository that empowers you to build websites using a wide range of popular programming languages and frameworks, including **Python, HTML, CSS, PHP, JavaScript, React, Go**, and more. Whether you want to rapidly prototype, learn cross-language website development, or deploy full-featured sites, web-maker provides a unified toolkit for your needs.

---

## Features

- **Multi-Language Support:** Build websites with Python, PHP, Go, JavaScript (including React), and classic HTML/CSS.
- **Unified Workflow:** Easily switch between languages and frameworks within a single project.
- **Customizable Templates:** Start from pre-made templates or create your own.
- **Live Preview:** Instantly preview your website as you develop.
- **Fast Deployment:** Deploy your site to the web or export for your own hosting.
- **Extensible:** Add your own plugins or components as needed.

---

## Getting Started

### Prerequisites

Depending on your chosen stack, you may need to install:

- [Node.js](https://nodejs.org/) (for JavaScript/React projects)
- [Python](https://python.org/) (for Python-based sites)
- [Go](https://golang.org/) (for Go support)
- [PHP](https://www.php.net/) (for PHP templates)

Install only the languages you plan to use!

### Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/web-maker.git
cd web-maker
```

Install dependencies as needed:

```bash
npm install                 # For JavaScript/React
pip install -r requirements.txt   # For Python (if applicable)
# Add Go/PHP installation steps as needed
```

---

## Usage

Run the web-maker tool:

```bash
npm start
```
or
```bash
python main.py
```
or
```bash
go run main.go
```

> _Choose the command that matches your selected language/framework._

### Creating a Website

1. Select your preferred language or framework.
2. Pick a template or start from scratch.
3. Customize content, styles, and scripts.
4. Preview your site live.
5. Deploy to the web or export the output.

---

## Quick Start with Python CLI

A lightweight Python CLI called **webmaker.py** is included to help you scaffold projects instantly.

### List Available Templates

```bash
python webmaker.py list
```

### Create a New Project

```bash
python webmaker.py new <template> <project-name>
# example:
python webmaker.py new basic my-website
```

The command above copies everything from `templates/basic` into the `my-website/` folder and automatically replaces `{{project_name}}` placeholders.

Current built-in templates:

- `basic` – Plain HTML/CSS/JS starter.
- `flask` – Minimal Python Flask application.

> More templates (React, PHP, Go, etc.) will be added soon. Feel free to contribute your own in the `templates/` directory!

---

## Supported Languages & Frameworks

- **Python** (Flask, Django, etc.)
- **PHP**
- **Go**
- **JavaScript** (Vanilla, Node.js, React, etc.)
- **HTML/CSS**

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests to help improve web-maker.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For support or questions, open an issue
