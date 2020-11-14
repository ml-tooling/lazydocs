
<a href="../src/lazydocs/generator.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `lazydocs.generator`



---

<a href="../src/lazydocs/generator.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_md_file`

```python
to_md_file(string: str, filename: str, out_path: str = '') → None
```

Imports a module path and create an api doc file from it.


**Args:**


 - <b>`string`</b> (str):  String with line breaks to write to file.

 - <b>`filename`</b> (str):  Filename without the .md

 - <b>`out_path`</b> (str):  The output directory


---

<a href="../src/lazydocs/generator.py#L607"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `generate_docs`

```python
generate_docs(
    paths: List[str],
    output_path: str = '/docs',
    src_root_path: Optional[str] = None,
    src_base_url: Optional[str] = None,
    remove_package_prefix: bool = False,
    validate: bool = False
) → None
```

Generates markdown documentation for provided paths based on Google-style docstrings.


**Args:**


 - <b>`paths`</b>:  Selected paths or import name for markdown generation.

 - <b>`output_path`</b>:  The output path for the creation of the markdown files. Set this to `stdout` to print all markdown to stdout.

 - <b>`src_root_path`</b>:  The root folder name containing all the sources. Fallback to git repo root.

 - <b>`src_base_url`</b>:  The base url of the github link. Should include branch name. All source links are generated with this prefix.

 - <b>`remove_package_prefix`</b>:  If `True`, the package prefix will be removed from all functions and methods.

 - <b>`validate`</b>:  If `True`, validate the docstrings via pydocstyle. Requires pydocstyle to be installed.


---

<a href="../src/lazydocs/generator.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MarkdownAPIGenerator`




<a href="../src/lazydocs/generator.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    src_root_path: Optional[str] = None,
    src_base_url: Optional[str] = None,
    remove_package_prefix: bool = False
)
```

Initializes the markdown API generator.


**Args:**


 - <b>`src_root_path`</b>:  The root folder name containing all the sources.

 - <b>`src_base_url`</b>:  The base github link. Should include branch name.
 All source links are generated with this prefix.

 - <b>`remove_package_prefix`</b>:  If `True`, the package prefix will be removed from all functions and methods.



---

<a href="../src/lazydocs/generator.py#L436"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `class2md`

```python
class2md(cls: Any, depth: int = 2) → str
```

Takes a class and creates markdown text to document its methods and variables.


**Args:**


 - <b>`cls`</b> (class):  Selected class for markdown generation.

 - <b>`depth`</b> (int, optional):  Number of # to append to function name. Defaults to 2.


**Returns:**


 - <b>`str`</b>:  Markdown documentation for selected class.

---

<a href="../src/lazydocs/generator.py#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `doc2md`

```python
doc2md(obj: Any) → str
```

Parse docstring (with getdoc) according to Google-style formatting and convert to markdown.


**Args:**


 - <b>`obj`</b>:  Selected object for markdown generation.


**Returns:**


 - <b>`str`</b>:  Markdown documentation for docstring of selected object.

---

<a href="../src/lazydocs/generator.py#L371"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `func2md`

```python
func2md(func: Callable, clsname: str = '', depth: int = 3) → str
```

Takes a function (or method) and generates markdown docs.


**Args:**


 - <b>`func`</b> (Callable):  Selected function (or method) for markdown generation.

 - <b>`clsname`</b> (str, optional):  Class name to prepend to funcname. Defaults to "".

 - <b>`depth`</b> (int, optional):  Number of # to append to class name. Defaults to 3.


**Returns:**


 - <b>`str`</b>:  Markdown documentation for selected function.

---

<a href="../src/lazydocs/generator.py#L586"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `import2md`

```python
import2md(obj: Any, depth: int = 1) → str
```

Generates markdown documentation for a selected object/import.


**Args:**


 - <b>`obj`</b> (Any):  Selcted object for markdown docs generation.

 - <b>`depth`</b> (int, optional):  Number of # to append before heading. Defaults to 1.


**Returns:**


 - <b>`str`</b>:  Markdown documentation of selected object.

---

<a href="../src/lazydocs/generator.py#L511"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `module2md`

```python
module2md(module: module, depth: int = 1) → str
```

Takes an imported module object and create a Markdown string containing functions and classes.


**Args:**


 - <b>`module`</b> (types.ModuleType):  Selected module for markdown generation.

 - <b>`depth`</b> (int, optional):  Number of # to append before module heading. Defaults to 1.


**Returns:**


 - <b>`str`</b>:  Markdown documentation for selected module.


