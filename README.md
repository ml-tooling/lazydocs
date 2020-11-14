<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    lazydocs
</h1>

<p align="center">
    <strong>Generate markdown API documentation for Google-style Python docstring.</strong>
</p>

<p align="center">
    <a href="https://github.com/ml-tooling/lazydocs/commits/" title="Last Commit"><img src="https://img.shields.io/github/last-commit/ml-tooling/lazydocs?style=flat"></a>
    <a href="https://github.com/ml-tooling/lazydocs/issues" title="Open Issues"><img src="https://img.shields.io/github/issues/ml-tooling/lazydocs?style=flat"></a>
    <a href="https://github.com/ml-tooling/lazydocs/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://api.reuse.software/info/github.com/ml-tooling/lazydocs" title="REUSE status"><img src="https://api.reuse.software/badge/github.com/ml-tooling/lazydocs"></a>
    <a href="https://github.com/ml-tooling/lazydocs/actions?query=workflow%3Abuild-pipeline" title="Build status"><img src="https://github.com/ml-tooling/lazydocs/workflows/build-pipeline/badge.svg"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support--feedback">Support</a> •
  <a href="https://github.com/ml-tooling/lazydocs/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#contribution">Contribution</a> •
  <a href="https://github.com/ml-tooling/lazydocs/releases">Changelog</a>
</p>

Lazydocs makes it easy to generate beautiful markdown documentation for your Python API. It provides a simple command-line interface as well as a Python API to get full-fledged API documentation within seconds based on all of the [Google-style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) in your code. This markdown documentation can be pushed to Github or integrated into your MkDocs site.

## Highlights

- ⏱&nbsp; Simple CLI to generate markdown docs in seconds.
- 📋&nbsp; Supports [Google-style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- 📚&nbsp; Compatible with Github Markdown and MkDocs.

## Getting Started

_This section should contain the simplest and most basic way to run and use the project, preferably with one command._

```bash
lazydocs generate <path/to/package/or/module>
```

## Support & Feedback

This project is maintained by [Benjamin Räthlein](https://twitter.com/raethlein), [Lukas Masuch](https://twitter.com/LukasMasuch), and [Jan Kalkan](https://www.linkedin.com/in/jan-kalkan-b5390284/). Please understand that we won't be able to provide individual support via email. We also believe that help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                     | Channel                                              |
| ------------------------ | ------------------------------------------------------ |
| 🚨&nbsp; **Bug Reports**       | <a href="https://github.com/ml-tooling/lazydocs/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abug+sort%3Areactions-%2B1-desc+" title="Open Bug Report"><img src="https://img.shields.io/github/issues/ml-tooling/lazydocs/bug.svg?label=bug"></a>                                 |
| 🎁&nbsp; **Feature Requests**  | <a href="https://github.com/ml-tooling/lazydocs/issues?q=is%3Aopen+is%3Aissue+label%3Afeature+sort%3Areactions-%2B1-desc" title="Open Feature Request"><img src="https://img.shields.io/github/issues/ml-tooling/lazydocs/feature.svg?label=feature"></a>                                 |
| 👩‍💻&nbsp; **Usage Questions**   |  _tbd_ |
| 🗯&nbsp; **General Discussion** | _tbd_ |
| ❓&nbsp; **Other Requests** | <a href="mailto:team@mltooling.org" title="Email ML Tooling Team"><img src="https://img.shields.io/badge/email-ML Tooling-green?logo=mail.ru&style=flat-square&logoColor=white"></a> |

## Features

_Use this section for advertising the most important features and advantages of the project. Also, add screenshots or examples to showcase important features. The main purpose of this section is marketing._

## Documentation

_Either put the documentation here or use a deployed documentation site via mkdocs and link to the documentation._

## Contributors

_TODO: Add sourcerer [hall of fame](https://github.com/sourcerer-io/hall-of-fame) here._

## Contribution

- Pull requests are encouraged and always welcome. Read our [contribution guidelines](https://github.com/ml-tooling/lazydocs/tree/main/CONTRIBUTING.md) and check out [help-wanted](https://github.com/ml-tooling/lazydocs/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A"help+wanted"+sort%3Areactions-%2B1-desc+) issues.
- Submit Github issues for any [feature request and enhancement](https://github.com/ml-tooling/lazydocs/issues/new?assignees=&labels=feature&template=02_feature-request.md&title=), [bugs](https://github.com/ml-tooling/lazydocs/issues/new?assignees=&labels=bug&template=01_bug-report.md&title=), or [documentation](https://github.com/ml-tooling/lazydocs/issues/new?assignees=&labels=documentation&template=03_documentation.md&title=) problems.
- By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/ml-tooling/lazydocs/blob/main/.github/CODE_OF_CONDUCT.md).
- The [development section](#development) below contains information on how to build and test the project after you have implemented some changes.

## Development

> _**Requirements**: [Docker](https://docs.docker.com/get-docker/) and [Act](https://github.com/nektos/act#installation) are required to be installed on your machine to execute the build process._

To simplify the process of building this project from scratch, we provide build-scripts that run all necessary steps (build, check, test, and release) within a containerized environment. To build and test your changes, execute the following command in the project root folder:

```bash
act -j build
```

Refer to our [contribution guides](https://github.com/ml-tooling/lazydocs/blob/main/CONTRIBUTING.md#development-instructions) for more detailed information on our build scripts and development process.

---

Licensed **MIT**. Created and maintained with ❤️&nbsp; by developers from Berlin.
