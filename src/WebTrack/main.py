import sys
from PySide6 import QtWidgets, QtGui

from WebTrack import configs
from WebTrack.widgets import WebTrackWidget


def main():
    # custom style
    # qs = QtWidgets.QStyle()
    # qs.setProperty('background-color', 'red')
    # QtWidgets.QApplication.setStyle(qs)

    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('WebTrack')

    # Application Icon
    icon = QtGui.QIcon()
    icon.addFile(str(configs.APP_ICON))
    app.setWindowIcon(icon)

    widget = WebTrackWidget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
