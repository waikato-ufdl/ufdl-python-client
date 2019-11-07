Pypi
====

Preparation:
* increment version in `setup.py`
* add new changelog section in `CHANGES.rst`
* commit/push all changes

Commands for releasing on pypi-waikato (requires twine >= 1.8.0):

```
  rm dist/* src/ufdl-python-client.egg-info
  python setup.py clean
  python setup.py sdist
  twine upload --repository-url https://adams.cms.waikato.ac.nz/nexus/repository/pypi-waikato/ dist/*
```


Github
======

Steps:
* start new release (version: `vX.Y.Z`)
* enter release notes, i.e., significant changes since last release
* upload `ufdl-python-client-X.Y.Z.tar.gz` previously generated with `setup.py`
* publish
