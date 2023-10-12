# Changelog

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## To Do

- docs/implementation
- Django methods
- Graphene methods
- Django fields
- docs/integrations
- improve __repr__
- add strict version
    - prevent mixing definition forms
    - enforce consistent attributes across instances

## [Unreleased]

- renamed `label` attribute to `value`
- replaced `canonical_name` attribute and `cn` property with `cname` attribute
- removed `cn_lower` (adds no value)
- renamed `cn_title` to `cname_pretty`
- wrote docs/index
- wrote docs/customizing
- defined docs nav order
- replaced deepcopy strategy (for immutability) with `_attrdir`` dict + custom attribute access methods, which also facilitates attributes overriding existing properties and methods when collisions occur
- added `as_dict`, `all_dict`, `as_tuple`, and `all_tuple`

## [0.2.0] - 2023-10-09

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
