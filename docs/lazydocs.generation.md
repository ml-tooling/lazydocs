<!-- markdownlint-disable -->

<a href="../src/lazydocs/generation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `lazydocs.generation`
Main module for markdown generation.


## Table of Contents
- [`MarkdownGenerator`](./lazydocs.generation.md#class-markdowngenerator)
	- [`__init__`](./lazydocs.generation.md#constructor-__init__)
	- [`class2md`](./lazydocs.generation.md#method-class2md)
	- [`func2md`](./lazydocs.generation.md#method-func2md)
	- [`import2md`](./lazydocs.generation.md#method-import2md)
	- [`module2md`](./lazydocs.generation.md#method-module2md)
	- [`overview2md`](./lazydocs.generation.md#method-overview2md)
	- [`toc2md`](./lazydocs.generation.md#method-toc2md)
- [`generate_docs`](./lazydocs.generation.md#function-generate_docs)
- [`to_md_file`](./lazydocs.generation.md#function-to_md_file)



---

<a href="../src/lazydocs/generation.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `to_md_file`

```python
to_md_file(
    markdown_str: str,
    filename: str,
    out_path: str = '.',
    watermark: bool = True,
    disable_markdownlint: bool = True,
    is_mdx: bool = False
) → None
```

Creates an API docs file from a provided text.


**Args:**

- <b>`markdown_str`</b> (str): Markdown string with line breaks to write to file.
- <b>`filename`</b> (str): Filename without the .md
- <b>`out_path`</b> (str): The output directory.
- <b>`watermark`</b> (bool): If `True`, add a watermark with a timestamp to bottom of the markdown files.
- <b>`disable_markdownlint`</b> (bool): If `True`, an inline tag is added to disable markdownlint for this file.
- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.



---

<a href="../src/lazydocs/generation.py#L1158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `generate_docs`

```python
generate_docs(
    paths: List[str],
    output_path: str = './docs',
    src_root_path: Optional[str] = None,
    src_base_url: Optional[str] = None,
    remove_package_prefix: bool = False,
    ignored_modules: Optional[List[str]] = None,
    output_format: Optional[str] = None,
    overview_file: Optional[str] = None,
    watermark: bool = True,
    validate: bool = False,
    private_modules: bool = False,
    include_toc: bool = False,
    url_line_prefix: Optional[str] = None
) → None
```

Generates markdown documentation for provided paths based on Google-style docstrings.


**Args:**

- <b>`paths`</b>: Selected paths or import name for markdown generation.
- <b>`output_path`</b>: The output path for the creation of the markdown files. Set this to `stdout` to print all markdown to stdout.
- <b>`src_root_path`</b>: The root folder name containing all the sources. Fallback to git repo root.
- <b>`src_base_url`</b>: The base url of the github link. Should include branch name. All source links are generated with this prefix.
- <b>`remove_package_prefix`</b>: If `True`, the package prefix will be removed from all functions and methods.
- <b>`ignored_modules`</b>: A list of modules that should be ignored.
- <b>`output_format`</b>: Markdown file extension and format.
- <b>`overview_file`</b>: Filename of overview file. If not provided, no overview file will be generated.
- <b>`watermark`</b>: If `True`, add a watermark with a timestamp to bottom of the markdown files.
- <b>`validate`</b>: If `True`, validate the docstrings via pydocstyle. Requires pydocstyle to be installed.
- <b>`private_modules`</b>: If `True`, includes modules with `_` prefix.
- <b>`url_line_prefix: Line prefix for git repository line url anchors. Default`</b>: None - github "L".



---

<a href="../src/lazydocs/generation.py#L627"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `MarkdownGenerator`
Markdown generator class.


<a href="../src/lazydocs/generation.py#L630"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>constructor</kbd> `__init__`

```python
MarkdownGenerator(
    src_root_path: Optional[str] = None,
    src_base_url: Optional[str] = None,
    remove_package_prefix: bool = False,
    url_line_prefix: Optional[str] = None
)
```

Initializes the markdown API generator.


**Args:**

- <b>`src_root_path`</b>: The root folder name containing all the sources.
- <b>`src_base_url`</b>: The base github link. Should include branch name.
    All source links are generated with this prefix.
- <b>`remove_package_prefix`</b>: If `True`, the package prefix will be removed from all functions and methods.
- <b>`url_line_prefix: Line prefix for git repository line url anchors. Default`</b>: None - github "L".





---

<a href="../src/lazydocs/generation.py#L795"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `class2md`

```python
class2md(cls: Any, depth: int = 2, is_mdx: bool = False) → str
```

Takes a class and creates markdown text to document its methods and variables.


**Args:**

- <b>`cls`</b> (class): Selected class for markdown generation.
- <b>`depth`</b> (int, optional): Number of # to append to function name. Defaults to 2.
- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.


**Returns:**

- <b>`str`</b>: Markdown documentation for selected class.


---

<a href="../src/lazydocs/generation.py#L706"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `func2md`

```python
func2md(
    func: Callable,
    clsname: str = '',
    depth: int = 3,
    is_mdx: bool = False
) → str
```

Takes a function (or method) and generates markdown docs.


**Args:**

- <b>`func`</b> (Callable): Selected function (or method) for markdown generation.
- <b>`clsname`</b> (str, optional): Class name to prepend to funcname. Defaults to "".
- <b>`depth`</b> (int, optional): Number of # to append to class name. Defaults to 3.
- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.


**Returns:**

- <b>`str`</b>: Markdown documentation for selected function.


---

<a href="../src/lazydocs/generation.py#L1046"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `import2md`

```python
import2md(
    obj: Any,
    depth: int = 1,
    is_mdx: bool = False,
    include_toc: bool = False
) → str
```

Generates markdown documentation for a selected object/import.


**Args:**

- <b>`obj`</b> (Any): Selcted object for markdown docs generation.
- <b>`depth`</b> (int, optional): Number of # to append before heading. Defaults to 1.
- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.
- <b>`include_toc`</b> (bool, Optional): Include table of contents for module file. Defaults to False.


**Returns:**

- <b>`str`</b>: Markdown documentation of selected object.


---

<a href="../src/lazydocs/generation.py#L943"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `module2md`

```python
module2md(
    module: module,
    depth: int = 1,
    is_mdx: bool = False,
    include_toc: bool = False
) → str
```

Takes an imported module object and create a Markdown string containing functions and classes.


**Args:**

- <b>`module`</b> (types.ModuleType): Selected module for markdown generation.
- <b>`depth`</b> (int, optional): Number of # to append before module heading. Defaults to 1.
- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.
- <b>`include_toc`</b> (bool, optional): Include table of contents in module file. Defaults to False.


**Returns:**

- <b>`str`</b>: Markdown documentation for selected module.


---

<a href="../src/lazydocs/generation.py#L1068"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `overview2md`

```python
overview2md(is_mdx: bool = False) → str
```

Generates a documentation overview file based on the generated docs.


**Args:**

- <b>`is_mdx`</b> (bool, optional): JSX support. Default to False.


**Returns:**

- <b>`str`</b>: Markdown documentation of overview file.


---

<a href="../src/lazydocs/generation.py#L1137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `toc2md`

```python
toc2md(module: module = None, is_mdx: bool = False) → str
```

Generates table of contents for imported object.





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
