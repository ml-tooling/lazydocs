"""Command line interface of lazydocs."""

from typing import List, Optional

import typer

from lazydocs import generate_docs

app = typer.Typer()


@app.command()
def generate(
    paths: List[str] = typer.Argument(  # type: ignore
        ..., help="Selected paths or imports for markdown generation."
    ),
    output_path: str = typer.Option(
        "./docs/",
        help="The output path for the creation of the markdown files. Set this to `stdout` to print all markdown to stdout.",
    ),
    src_base_url: Optional[str] = typer.Option(
        None,
        help="The base repo link used as prefix for all source links. Should also include the branch name.",
    ),
    overview_file: Optional[str] = typer.Option(
        None,
        help="Filename of overview file. If not provided, no API overview file will be generated.",
    ),
    remove_package_prefix: bool = typer.Option(
        True,
        help="If `True`, the package prefix will be removed from all functions and methods.",
    ),
    ignored_modules: List[str] = typer.Option(
        [],
        help="A list of modules that should be ignored.",
    ),
    watermark: bool = typer.Option(
        True,
        help="If `True`, add a watermark with a timestamp to bottom of the markdown files.",
    ),
    validate: bool = typer.Option(
        False,
        help="If `True`, validate the docstrings via pydocstyle. Requires pydocstyle to be installed.",
    ),
    output_format: Optional[str] = typer.Option(
        None,
        help="The output format for the creation of the markdown files. This may be 'md' or 'mdx'. Defaults to md.",
    ),
    private_modules: bool = typer.Option(
        False,
        help="If `True`, all packages starting with `_` will be included.",
    ),
) -> None:
    """Generates markdown documentation for your Python project based on Google-style docstrings."""

    try:
        generate_docs(
            paths=paths,
            output_path=output_path,
            src_base_url=src_base_url,
            remove_package_prefix=remove_package_prefix,
            ignored_modules=ignored_modules,
            output_format=output_format,
            overview_file=overview_file,
            watermark=watermark,
            validate=validate,
            private_modules=private_modules,
        )
    except Exception as ex:
        typer.echo(str(ex))
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
