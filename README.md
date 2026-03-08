Based on https://github.com/edwardtheharris/sphinxcontrib.youtube, https://github.com/divi255/sphinxcontrib.youtube/,
and the original https://github.com/shomah4a/sphinxcontrib.youtube.

[![PyPI - Version](https://img.shields.io/pypi/v/enginehub.sphinx-youtube)](https://pypi.org/project/enginehub.sphinx-youtube/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enginehub.sphinx-youtube)

Install:

```shell
pip install enginehub.sphinx_youtube
```

Usage:

First of all, add `enginehub.sphinx_youtube` to sphinx extension list in conf.py:
```python
extensions = ['enginehub.sphinx_youtube']
```
then use `youtube` directive.

You can specify video by video url or video id:
```rst
.. youtube:: https://www.youtube.com/watch?v=Ql9sn3aLLlI

.. youtube:: Ql9sn3aLLlI
```
