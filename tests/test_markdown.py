import shutil
import textwrap
from pathlib import Path

import pytest
from lazydocs import generate_docs

CURDIR = Path(__file__).parent
OUTPUT = CURDIR / "output"

CODE_BLOCK = """\
```python
from example import a_public_function

obj = a_public_function(100)
print(obj.enum_value)
```
"""


@pytest.fixture(scope="session")
def markdown():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)

    generate_docs(
        paths=[str(CURDIR / "resources")],
        output_path=str(OUTPUT),
        src_base_url="https://www.github.com/exampleorg/examplerepo",
        remove_package_prefix=True,
        overview_file=None,
        watermark=False,
        validate=True,
    )

    with open(OUTPUT / "example.md") as fd:
        yield fd.read()


def test_dataclass(markdown):
    assert "## class `ADataClass`" in markdown


def test_enum(markdown):
    assert "## enum `AnEnum`" in markdown


def test_base_url(markdown):
    assert (
        "https://www.github.com/exampleorg/examplerepo/tests/resources/example/__init__.py"
        in markdown
    )


def test_trailing_whitespace(markdown):
    for line in markdown.splitlines():
        assert not line.endswith(" ")


def test_whitespace_multiline(markdown):
    assert "are appended together correctly" in markdown
    assert "should make it into a space" in markdown


def test_code_block(markdown):
    code = textwrap.dedent(CODE_BLOCK)
    assert code in markdown


def test_multiple_paragraphs(markdown):
    paragraph = "\nThis is a second paragraph that should be separate.\n"
    assert paragraph in markdown, markdown


def test_source_link(markdown):
    assert "_class.py:9" in markdown
