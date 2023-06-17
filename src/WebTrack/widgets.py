import sys

from PySide6 import QtCore, QtWidgets, QtGui


class WebTrackWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout(self)
        # self.layout.setDirection(
        #     QtWidgets.QBoxLayout.Direction.TopToBottom
        # )

        self.main_menu_bar = QtWidgets.QMenuBar(self)
        self.main_menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: red;
                margin: 0;
                margin-left: 0;
                padding: 0;
                bottom: 0;
            }
        """)
        # self.main_menu_bar.setMaximumHeight(30)
        # self.setLayoutDirection(QtCore.Qt.LayoutDirection.LayoutDirectionAuto)

        file_menu = QtWidgets.QMenu('File', self)
        # Sub Menu Items
        new_project_action = QtGui.QAction('New Project', self)
        new_project_action.triggered.connect(self.new_project_action)
        file_menu.addAction(new_project_action)

        file_menu.addMenu('Recent Projects')
        exit_act = QtGui.QAction('Exit', self)
        exit_act.triggered.connect(self.exit)
        file_menu.addAction(exit_act)

        self.main_menu_bar.addMenu(file_menu)
        self.main_menu_bar.addMenu('View')
        self.main_menu_bar.addMenu('Tools')
        self.main_menu_bar.addMenu('Help')

        self.layout.setMenuBar(self.main_menu_bar)

        # Create Tabs Widget
        self.tabs = QtWidgets.QTabWidget(self)
        self.layout.addWidget(self.tabs)

        # self.text = QtWidgets.QLabel(
        #     'WebTrack', alignment=QtCore.Qt.AlignCenter
        # )
        # self.layout.addWidget(self.text)

    def __init_project_tab(self, dlg: QtWidgets.QInputDialog):
        tab = QtWidgets.QWidget(self)
        tab.setWindowTitle(dlg.textValue())
        self.tabs.addTab(tab, dlg.textValue())
        # BoxLayout for project configuration
        self.project_layout = QtWidgets.QBoxLayout(
            QtWidgets.QBoxLayout.Direction.LeftToRight
        )

        # Input Dialog
        self.project_path = QtWidgets.QLineEdit()
        # QtCore.Qt.WidgetAttribute
        label = QtWidgets.QLabel("Project Dir")
        label.setText(f"<font color='red'>*</font> {label.text()}")
        label.setStyleSheet('QLabel {color: black;}')
        self.project_layout.addWidget(label)
        self.project_path.setDragEnabled(True)
        self.project_path.setEnabled(True)
        self.project_path.setFocus()
        self.project_path.setPlaceholderText('Enter Absolute Path')
        self.project_path.setStyleSheet("""
                    QLineEdit { 
                        width: 100%;
                        background-color: white;
                        color: black; 
                    }
                """)

        # self.project_path.setAccessibleName('Choose Project Directory')
        # self.project_path = QtWidgets.QInputDialog()
        # self.project_path.setOption(
        #     QtWidgets.QInputDialog.InputDialogOption.NoButtons, True
        # )
        # self.project_path.setInputMode(
        #     QtWidgets.QInputDialog.InputMode.TextInput
        # )
        # self.project_path.setMaximumWidth(300)
        # self.project_path.setLabelText('Choose Project Directory')
        # Button for Input Dialog
        self.btn_chd = QtWidgets.QPushButton("Open")
        self.btn_chd.setMaximumWidth(100)
        self.btn_chd.clicked.connect(self.choose_dir)

        self.project_layout.addWidget(self.project_path)
        self.project_layout.addWidget(self.btn_chd)

        tab.setLayout(self.project_layout)

        self.tabs.update()
        self.layout.update()

    @QtCore.Slot()
    def choose_dir(self):
        file_dialog = QtWidgets.QFileDialog()
        self.project_path.setText(file_dialog.getExistingDirectory())

    @QtCore.Slot()
    def new_project_action(self):
        dlg = QtWidgets.QInputDialog()
        dlg.setWindowTitle('New Project')
        dlg.setMaximumWidth(400)
        dlg.setMaximumHeight(200)

        if dlg.exec_():
            # Remove Text Notification Widget
            # self.layout.removeWidget(self.text)
            self.__init_project_instance(dlg)
        else:
            print("Cancel!")

    @QtCore.Slot()
    def exit(self, s):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Exit')
        msg_box.setText('Do you want to exit the application?')
        exit_btn = msg_box.addButton(
            'Exit', QtWidgets.QMessageBox.ButtonRole.YesRole
        )
        msg_box.addButton(
            'Cancel', QtWidgets.QMessageBox.ButtonRole.RejectRole
        )
        msg_box.exec_()

        if msg_box.clickedButton() == exit_btn:
            sys.exit(s)

    def closeEvent(self, event):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Exit')
        msg_box.setText('Do you want to exit the application?')
        exit_btn = msg_box.addButton(
            'Exit', QtWidgets.QMessageBox.ButtonRole.YesRole
        )
        cancel_btn = msg_box.addButton(
            'Cancel', QtWidgets.QMessageBox.ButtonRole.RejectRole
        )
        msg_box.exec_()

        if msg_box.clickedButton() == exit_btn:
            event.accept()
        elif msg_box.clickedButton() == cancel_btn:
            event.ignore()
