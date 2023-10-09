# Changelog

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## To Do

- rename package to `simpleset`
- improve output of `Object.__repr__`
- add custom Django fields

## [Unreleased]

- rewrote docs for v0.1.0 API

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

[unreleased]: https://github.com/odigity/py-objects/compare/v0.0.3...HEAD
[0.1.0]: https://github.com/odigity/py-objects/compare/v0.0.3...v0.1.0
[0.0.3]: https://github.com/odigity/py-objects/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/odigity/py-objects/releases/tag/v0.0.2
