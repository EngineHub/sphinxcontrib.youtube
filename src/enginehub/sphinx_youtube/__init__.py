#-*- coding:utf-8 -*-

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
