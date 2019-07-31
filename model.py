import os

import maya.api.OpenMaya as om
from PySide2 import QtCore, QtGui, QtWidgets
from qt_helper.load_ui import loadUi
from qt_helper.maya_dockable_window import MayaDockableWidget

from .core import utils

UI_FILE = os.path.join(os.path.dirname(__file__), "resources", "ui", "main.ui")


class ABCExporterWindow(MayaDockableWidget, QtWidgets.QWidget):

    APP_NAME = "ABCExporter"
    # WIDTH = 258
    # HEIGHT = 500

    def __init__(self, parent=None):
        super(ABCExporterWindow, self).__init__(parent=parent)
        loadUi(UI_FILE, self)

        self._callbacks = self._register_callbacks()

    def _register_callbacks(self):
        callbacks = [
            om.MEventMessage.addEventCallback("SelectionChanged", self._maya_selection_changed)
        ]
        return callbacks

    def _maya_selection_changed(self, *args, **kwargs):
        selection = utils.get_selection()
        self._populate_dag_nodes(dag_nodes=selection)

    def closeEvent(self, *args, **kwargs):
        for callback in self._callbacks:
            om.MEventMessage.removeCallback(callback)
        super(ABCExporterWindow, self).closeEvent(*args, **kwargs)

    def _populate_dag_nodes(self, dag_nodes):
        self.dag_nodes_listwidget.clear()
        for node in dag_nodes:
            short_name = node.split("|")[-1]
            list_item = QtWidgets.QListWidgetItem()
            list_item.setText(short_name)
            list_item.setData(QtCore.Qt.UserRole, node)
            self.dag_nodes_listwidget.addItem(list_item)
