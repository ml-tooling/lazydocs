import hashlib

from lazydocs import MarkdownGenerator


def test_import2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.import2md(MarkdownGenerator.import2md)
    md_hash = hashlib.md5(markdown.encode("utf-8")).hexdigest()
    assert md_hash == "4a2b89327414077031d103b4cf6672b6"
