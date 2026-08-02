from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

class DashboardPage(QWidget):

    def __init__(
    self,
    abrir_static_records,
    abrir_vinyl_black,
    abrir_notes,
    abrir_status,
    abrir_settings,
    cerrar_app,
    ):
        super().__init__()

        self.abrir_static_records = abrir_static_records
        self.abrir_vinyl_black = abrir_vinyl_black
        self.abrir_notes = abrir_notes
        self.abrir_status = abrir_status
        self.abrir_settings = abrir_settings
        self.cerrar_app = cerrar_app

        self.crear_interfaz()

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(40,30,40,30)
        layout_principal.setSpacing(20)

        titulo = QLabel("MangOS MAINFRAME NX-01")
        titulo.setObjectName("TitleLabel")

        subtitulo = QLabel("Static Records Edition // Graphical Shell v0.1")
        subtitulo.setObjectName("SubtitleLable")

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(subtitulo)

        panel_estado = self.crear_panel_estado()
        layout_principal.addWidget(panel_estado)

        panel_apps = self.crear_panel_apps()
        layout_principal.addWidget(panel_apps)

        layout_principal.addStretch()

        footer = QLabel("LOCAL-FIRST CYBERDECK OPERATING ENVIRONMENT")
        footer.setObjectName("SubtitleLabel")
        layout_principal.addWidget(footer)

        self.setLayout(layout_principal)

    def crear_panel_estado(self):
        panel = QFrame()
        panel.setObjectName("Panel")

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)

        titulo = QLabel("SYSTEM STATUS")
        titulo.setObjectName("SectionTitle")
        layout.addWidget(titulo)

        estados = [
            "CORE SYSTEM        ONLINE",
            "BOOT MODE          DEVELOPMENT",
            "STATIC RECORDS     READY",
            "VINYL BLACK.FM     READY",
            "NOTES              READY SOON",
        ]

        for estado in estados:
            label = QLabel(estado)
            label.setObjectName("StatusText")
            layout.addWidget(label)

        panel.setLayout(layout)

        return panel

    def crear_panel_apps(self):
        panel = QFrame()
        panel.setObjectName("Panel")

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(15)

        titulo = QLabel("APPLICATIONS")
        titulo.setObjectName("SectionTitle")
        layout.addWidget(titulo)

        fila_1 = QHBoxLayout()
        fila_2 = QHBoxLayout()

        btn_static_records = QPushButton("STATIC RECORDS")
        btn_vinylblack = QPushButton("VINYL BLACK.FM")
        btn_notes = QPushButton("NOTES")

        btn_status = QPushButton("SYSTEM STATUS")
        btn_settings = QPushButton("SETTINGS")
        btn_exit = QPushButton("EXIT")

        btn_static_records.clicked.connect(self.abrir_static_records)
        btn_vinylblack.clicked.connect(self.abrir_vinyl_black)
        btn_notes.clicked.connect(self.abrir_notes)
        btn_status.clicked.connect(self.abrir_status)
        btn_settings.clicked.connect(self.abrir_settings)
        btn_exit.clicked.connect(self.cerrar_app)

        fila_1.addWidget(btn_static_records)
        fila_1.addWidget(btn_vinylblack)
        fila_1.addWidget(btn_notes)

        fila_2.addWidget(btn_status)
        fila_2.addWidget(btn_settings)
        fila_2.addWidget(btn_exit)

        layout.addLayout(fila_1)
        layout.addLayout(fila_2)

        panel.setLayout(layout)

        return panel
