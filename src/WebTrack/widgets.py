import sys

from PySide6 import QtCore, QtWidgets, QtGui


class WebTrackTabWidget(QtWidgets.QWidget):

    def __init__(self, title):
        super().__init__()
        self.title = title
        self.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LayoutDirectionAuto
        )
        self.setStyleSheet("""
            QWidget {
                background-color: green;
            }
        """)
        self.setWindowTitle(self.title)


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
        # self.tabs.setLayoutDirection(
        #     QtCore.Qt.LayoutDirection.LayoutDirectionAuto
        # )
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.layout.addWidget(self.tabs)

        # self.text = QtWidgets.QLabel(
        #     'WebTrack', alignment=QtCore.Qt.AlignCenter
        # )
        # self.layout.addWidget(self.text)

    @QtCore.Slot()
    def close_tab(self, index):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Exit')
        title = self.tabs.widget(index).title
        msg_box.setText(f'Do you want to close the {title} tab?')
        exit_btn = msg_box.addButton(
            'Exit', QtWidgets.QMessageBox.ButtonRole.YesRole
        )
        msg_box.addButton(
            'Cancel', QtWidgets.QMessageBox.ButtonRole.RejectRole
        )
        msg_box.exec_()

        if msg_box.clickedButton() == exit_btn:
            self.tabs.removeTab(index)

    def _init_project_tab(self, dlg: QtWidgets.QInputDialog):
        self.tab = WebTrackTabWidget(title=dlg.textValue())
        self.tabs.addTab(self.tab, dlg.textValue())
        # BoxLayout for project configuration
        # self.project_layout = QtWidgets.QBoxLayout(
        #     QtWidgets.QBoxLayout.Direction.LeftToRight
        # )
        self.project_layout = QtWidgets.QFormLayout()
        # x=0, y=0, w=0, h=0
        # self.setGeometry(0, 0, 800, 600)

        # Input Dialog
        self.project_path = QtWidgets.QLineEdit()
        # QtCore.Qt.WidgetAttribute
        label_pp = QtWidgets.QLabel("Project Dir")
        label_pp.setText(f"<font color='red'>*</font> {label_pp.text()}")
        label_pp.setStyleSheet('QLabel {color: black;}')

        # self.project_layout.addWidget(label)
        self.project_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, label_pp
        )

        self.project_path.setDragEnabled(True)
        self.project_path.setEnabled(True)
        self.project_path.setFocus()
        self.project_path.setPlaceholderText('Enter Absolute Path')
        self.project_path.setStyleSheet("""
            QLineEdit { 
                width: 100%;
                background-color: white;
                color: black; 
                margin-top: 0;
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

        # Button for Input Dialog
        website = QtWidgets.QLineEdit()
        label_ws = QtWidgets.QLabel("Website")
        label_ws.setText(f"<font color='red'>*</font> {label_ws.text()}")
        label_ws.setStyleSheet('QLabel {color: black;}')

        self.project_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, label_ws
        )
        self.project_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, website
        )

        self.enable_selenium = QtWidgets.QCheckBox()
        self.enable_selenium.setText('Enable Selenium')
        self.enable_selenium.setToolTip('Enable Selenium Driver')
        self.project_layout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_selenium
        )
        self.enable_selenium.clicked.connect(self.show_driver_path)
        self.selenium_driver_path = QtWidgets.QLineEdit()
        self.sdp_label = QtWidgets.QLabel("Driver Path")
        self.sdp_label.setText(f"<font color='red'>*</font> {self.sdp_label.text()}")
        self.sdp_label.setStyleSheet('QLabel {color: black;}')

        # self.project_layout.addWidget(self.project_path)
        # self.project_layout.addWidget(self.btn_chd)
        self.project_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.project_path
        )
        self.project_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btn_chd
        )

        self.tab.setLayout(self.project_layout)

        self.tabs.update()
        self.layout.update()

    @QtCore.Slot()
    def choose_dir(self):
        file_dialog = QtWidgets.QFileDialog()
        self.project_path.setText(file_dialog.getExistingDirectory())

    @QtCore.Slot()
    def show_driver_path(self, checked):
        if checked:
            self.project_layout.setWidget(
                4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sdp_label
            )
            self.project_layout.setWidget(
                4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.selenium_driver_path
            )
        else:
            self.project_layout.removeWidget(self.sdp_label)
            self.project_layout.removeWidget(self.selenium_driver_path)
            self.project_layout.update()
            self.tab.update()
            self.tabs.update()
            self.layout.update()

    @QtCore.Slot()
    def new_project_action(self):
        dlg = QtWidgets.QInputDialog()
        dlg.setWindowTitle('New Project')
        dlg.setMaximumWidth(400)
        dlg.setMaximumHeight(200)

        if dlg.exec_():
            # Remove Text Notification Widget
            # self.layout.removeWidget(self.text)
            self._init_project_tab(dlg)
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
