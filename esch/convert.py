# convert.py
#   convert function for esch
# by: Noah Syrkis


# imports
from pathlib import Path
import subprocess
import frontmatter
from importlib import resources
import os


# contants
kinds = "slide book resume letter paper invoice proposal portfolio".split()
zotero = Path("~/Zotero").expanduser()
library = Path("~/code/esch/library.bib").expanduser()  # temporary hard coded
templates = Path("~/code/esch/templates").expanduser()  # temporary hard coded
filters = Path("~/code/esch/filters").expanduser()  # temporary hard coded


# functions
def config_fn(path, doc_type):
    if doc_type != "book":
        with open(path) as f:
            fm = frontmatter.load(f)
    return {
        **(fm.metadata if doc_type != "book" else {}),
        "doc_type": doc_type,
        "zotero": str(zotero),
        "library": str(library),
        "template": str(templates / f"{doc_type}.tex"),
        "filters": str(filters),
        "bibfile": str(library),
    }


def convert_fn(f, doc_type):
    path = Path(f).resolve()

    # Get the script path using importlib.resources
    with resources.path("esch.scripts", f"{doc_type}.sh") as script_path:
        script = str(script_path)

    # change dir to the file's directory
    old_dir = Path.cwd()
    os.chdir(path.parent)

    filebase = str(path.with_suffix(""))
    config = str(config_fn(path, doc_type)).replace("'", '"')

    # Change working directory to the Markdown file's directory
    command = [script, filebase, config]
    subprocess.run(command, check=True)

    os.chdir(old_dir)

    # Change back to the original directory
    return filebase + ".pdf"
