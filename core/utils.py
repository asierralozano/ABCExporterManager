import os

import maya.cmds as MC


def get_cache_folder():
    workspace = MC.workspace(q=True, dir=True) #pylint: disable=assignment-from-no-return
    return os.path.join(workspace, "cache", "alembic")


def generate_abc_path(folder, node):
    if "|" in node:
        node = node.split("|")[-1]
    return os.path.join(folder, "{}.abc".format(node))


def get_frame_range():
    min = MC.playbackOptions(q=True, min=True)
    max = MC.playbackOptions(q=True, max=True)
    return min, max


def get_selection():
    return MC.ls(sl=True, l=True)