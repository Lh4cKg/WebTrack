from PySide6 import QtCore, QtWidgets


class WebTrackWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.main_menu_bar = QtWidgets.QMenuBar()
        file_menu = QtWidgets.QMenu('File')
        file_menu.addMenu('New')
        file_menu.addMenu('Recent Projects')
        self.main_menu_bar.addMenu(file_menu)
        self.main_menu_bar.addMenu('View')
        self.main_menu_bar.addMenu('Tools')
        self.main_menu_bar.addMenu('Help')
        self.layout.setMenuBar(self.main_menu_bar)

        tabs = QtWidgets.QTabBar()
        # tab = QtWidgets.QTabWidget()
        # tab.setTabText('Projects Tabs')
        # tabs.setTabText(0, 'Projects Tabs')
        tabs.addTab('tab 1')
        # tabs.addTab('tab 2')
        self.layout.addWidget(tabs)

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

        self.layout.addLayout(self.project_layout)

        self.text = QtWidgets.QLabel(
            'WebTrack', alignment=QtCore.Qt.AlignCenter
        )
        self.layout.addWidget(self.text)

    @QtCore.Slot()
    def choose_dir(self):
        file_dialog = QtWidgets.QFileDialog()
        self.project_path.setText(file_dialog.getExistingDirectory())
