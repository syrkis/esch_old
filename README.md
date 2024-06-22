# esch

Streamlined document conversion using Pandoc and LaTeX.

## Features

- Convert Markdown to various document types (letter, paper, slides, etc.)
- Customizable templates and filters
- YAML frontmatter support
- Zotero integration for citations

## Installation

```bash
pip install esch
```

## Usage

```bash
esch letter document.md
esch slides presentation.md
esch paper research.md
```

## Configuration

Edit `config.json` to set paths for Zotero, templates, and filters.

## Requirements

- Python 3.11+
- Pandoc
- LaTeX
- Zotero (optional, for citations)

## License

MIT