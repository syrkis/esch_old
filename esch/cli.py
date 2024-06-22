import click
from pathlib import Path
from .convert import convert_fn, kinds


@click.command()
@click.argument("doc_type", type=click.Choice(kinds))
@click.argument("path", type=click.Path(exists=True))
def main(doc_type, path):
    """
    Convert markdown files to various formats using Pandoc.

    DOC_TYPE can be one of: book, paper, slide, letter, report, resume, invoice, proposal, portfolio

    PATH is the path to the file or directory (for books) to be converted
    """
    click.echo(f"Converting {path} to {doc_type} format...")
    output_file = convert_fn(path, doc_type)
    click.echo(f"Conversion complete! Output file: {output_file}")


if __name__ == "__main__":
    main()
