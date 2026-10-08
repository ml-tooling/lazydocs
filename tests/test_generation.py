import hashlib

from lazydocs import MarkdownGenerator


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
