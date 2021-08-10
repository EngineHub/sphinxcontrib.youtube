3#-*- coding:utf-8 -*-
u'''
embedding youtube video to sphinx

usage:

First of all, add `enginehub.youtube` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['enginehub.sphinx_youtube']


then use `youtube` directive.

You can specify video by video url or video id.

.. code-block:: rst

   .. youtube:: http://www.youtube.com/watch?v=Ql9sn3aLLlI

   .. youtube:: Ql9sn3aLLlI


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''

__version__ = '0.2.3'
__author__ = '@shomah4a'
__license__ = 'LGPLv3'


def skip_visit(_, _ignore2):
    from docutils.nodes import SkipNode
    raise SkipNode()


def setup(app):

    from . import youtube

    app.add_node(youtube.youtube,
                 html=(youtube.visit, youtube.depart),
                 latex=(skip_visit, None),
                 text=(skip_visit, None),
                 man=(skip_visit, None))

    app.add_directive('youtube', youtube.YoutubeDirective)
    return {'parallel_read_safe': True}
