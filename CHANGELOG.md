# Changelog

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## To Do

- docs/index
- docs/customizing
- docs/implementation
- Django methods
- Graphene methods
- Django fields
- docs/integrations
- reorder docs
- cleanup use of `==` vs `is`

## [Unreleased]


## [0.2.0] - 2023-10-09

- rewrote docs for v0.1.0 API
- renamed package to `simpleset`
- renamed `Object` to `Constant`
- renamed `Object.define` to `Constant.define_set`
- renamed `ErrorSet` to `Error`
- rewrote `Error` to subclass from itself (`define_family`, `define_children`)
- wrote docs/cheatsheet
- wrote docs/error

## [0.1.0] - 2023-10-09

- complete rewrite to combine Object + ObjectMananger into single class and simplify API
- added changelog
- added changelog link to `pyproject.toml` for PyPI
- added [pytest](https://pypi.org/project/pytest/) to dev dependencies
- configured pytest in `pyproject.toml` and `tests/conftest.py`
- converted `test.py` to a pytest test suite stored under `tests/`
- rewrote README to act as a preview of the docs

## [0.0.3] - 2023-10-08

- added `docs/` and `mkdocs.yml` for [MkDocs](https://mkdocs.org/) (intitial version identical to README)
- added `.readthedocs.yaml` for integration with [Read the Docs](https://readthedocs.org/)
- added documentation link to `pyproject.toml` for PyPI

## [0.0.2] - 2023-03-27

- first working version

[unreleased]: https://github.com/odigity/simpleset/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/odigity/simpleset/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/odigity/simpleset/compare/v0.0.3...v0.1.0
[0.0.3]: https://github.com/odigity/simpleset/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/odigity/simpleset/releases/tag/v0.0.2
