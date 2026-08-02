from PySide6.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout, QFrame


class SimplePage(QWidget):

    def __init__(self,titulo,subtitulo,descripcion, volver_callback):
        super().__init__()

        self.titulo = titulo
        self.subtitulo = subtitulo
        self.descripcion = descripcion
        self.volver_callback = volver_callback

        self.crear_interfaz()

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(40,30,40,30)
        layout_principal.setSpacing(20)

        titulo = QLabel(self.titulo)
        titulo.setObjectName("TitleLabel")

        subtitulo = QLabel(self.subtitulo)
        subtitulo.setObjectName("SubtitleLabel")

        panel = QFrame()
        panel.setObjectName("Panel")

        layout_panel = QVBoxLayout()
        layout_panel.setContentsMargins(20,20,20,20)
        layout_panel.setSpacing(15)

        descripcion = QLabel(self.descripcion)
        descripcion.setObjectName("StatusText")
        descripcion.setWordWrap(True)

        boton_volver = QPushButton("BACK TO MAINFRAME")
        boton_volver.clicked.connect(self.volver_callback)

        layout_panel.addWidget(descripcion)
        layout_panel.addWidget(boton_volver)

        panel.setLayout(layout_panel)

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(subtitulo)
        layout_principal.addWidget(panel)
        layout_principal.addStretch()

        self.setLayout(layout_principal)



