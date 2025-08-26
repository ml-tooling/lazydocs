import hashlib

from lazydocs import MarkdownGenerator, generate_docs
from tempfile import TemporaryDirectory


def test_import2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.import2md(MarkdownGenerator.import2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "4f5254f4be4158f984b7a9741d118698"


def test_class2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.class2md(MarkdownGenerator)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "ea0ad63a9018a85d8d76f9a6ad7f7985"


def test_module2md() -> None:
    generator = MarkdownGenerator()
    from lazydocs import generation

    markdown = generator.module2md(generation)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "e4637206eb4f1fb27360eed8cb3d99e2"


def test_func2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.func2md(MarkdownGenerator.func2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "797bad8c00ee6f189cb6f578eaec02c4"


def test_integration_generate_docs(capsys) -> None:
    with TemporaryDirectory() as d:
        test_module_name = "test_module"
        with open(f"{d}/{test_module_name}.py", "w") as f:
            f.write("")

        overview_file_name = "DOCS.md"
        overview_file = f"{d}/output/{overview_file_name}"
        generate_docs(
            paths=[d],
            output_path=f"{d}/output/",
            overview_file=overview_file_name
        )

        captured = capsys.readouterr()

        with open(overview_file) as f:
            result = f.read()

        assert test_module_name in result
        assert "Failed to generate docs for module" not in captured.out
