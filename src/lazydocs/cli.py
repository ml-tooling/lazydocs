from typing import List, Optional

import typer

import lazydocs.generator

app = typer.Typer()


@app.command()
def generate(
    paths: List[str] = typer.Argument(
        ..., help="Selected paths or import name for markdown generation."
    ),
    output_path: str = typer.Option(
        "./docs/",
        help="The output path for the creation of the markdown files. Set this to `stdout` to print all markdown to stdout.",
    ),
    github_link: Optional[str] = typer.Option(
        None,
        help="The base github link. Should include branch name. All source links are generated with this prefix.",
    ),
    remove_package_prefix: bool = typer.Option(
        True,
        help="If `True`, the package prefix will be removed from all functions and methods.",
    ),
    validate: bool = typer.Option(
        False,
        help="If `True`, validate the docstrings via pydocstyle. Requires pydocstyle to be installed.",
    ),
) -> None:
    """Generates markdown documentation for provided path based on Google-style docstrings."""

    lazydocs.generator.generate_docs(
        paths=paths,
        output_path=output_path,
        src_base_url=github_link,
        remove_package_prefix=remove_package_prefix,
        validate=validate,
    )


if __name__ == "__main__":
    app()
