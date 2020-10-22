"""
@author: Zlatko Minev
@date: 2020
"""


from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolBar
import time

class QToolBarExpanding(QToolBar):
    """
    `QToolBarExpanding` class extends the `QToolBar` class.

    Example:
        ```toolbar = gui.ui.toolBarView```

    Arguments:
        QToolbar (QToolbar): QToolbar
    """

    def expand_me(self):
        """Expand the toolbar"""
        if self.orientation() == Qt.Vertical:
            tool_style =  Qt.ToolButtonTextBesideIcon
            align = Qt.AlignLeft|Qt.AlignVCenter
        else: # Qt.Horizontal
            tool_style =  Qt.ToolButtonTextUnderIcon
            align = Qt.AlignHCenter|Qt.AlignTop

        # show icons and text
        self.setToolButtonStyle(tool_style)

        # align icons and text
        layout = self.layout()
        layout.setAlignment(align)
        layout.setSpacing(layout.spacing())
        for i in range(layout.count()):
            tool = layout.itemAt(i)
            tool.setAlignment(align)
            # https://doc.qt.io/qt-5/qlayoutitem.html#setAlignment

    def contract_me(self):
        """Contract the toolbar"""
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def enterEvent(self, evt: QtCore.QEvent) -> None:
        """enterEvent() is called when the mouse enters the widget's screen space.
         (This excludes screen space owned by any of the widget's children.)

        Arguments:
            evt (QtCore.QEvent): QtCore event
        """
        # should ideally have a timeout thread
        # print('-> Enter')
        self.expand_me()

        super().enterEvent(evt)

    def leaveEvent(self, evt: QtCore.QEvent) -> None:
        """leaveEvent() is called when the mouse leaves the widget's screen space.
        If the mouse enters a child widget it will not cause a leaveEvent().

        Arguments:
            evt (QtCore.QEvent): QtCore event
        """
        # print('<- EXIT')
        # this adds a 0.25sec delay before contracting the widget if mouse accidentally leaves
        time.sleep(0.25) 
        self.contract_me()
        super().leaveEvent(evt)
