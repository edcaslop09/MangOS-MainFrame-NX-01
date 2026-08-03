from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLineEdit,
    QTextEdit,
    QListWidget,
    QMessageBox,
)

from apps.notes.notes_manager import NotesManager



class NotesPage(QWidget):

    def __init__(self,volver_callback):
        super().__init__()

        self.volver_callback = volver_callback
        self.notes_manager = NotesManager()
        self.notas = []

        self.crear_interfaz()
        self.cargar_lista_notas()

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(40,30,40,30)
        layout_principal.setSpacing(20)

        titulo = QLabel("NOTES")
        titulo.setObjectName("TitleLabel")

        subtitulo = QLabel("Local-first notes app")
        subtitulo.setObjectName("SubtitleLabel")

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(subtitulo)

        contenido_layout = QHBoxLayout()
        contenido_layout.setSpacing(20)

        panel_lista = self.crear_panel_lista()
        panel_editor = self.crear_panel_editor()

        contenido_layout.addWidget(panel_lista,1)
        contenido_layout.addWidget(panel_editor,2)

        layout_principal.addLayout(contenido_layout)

        boton_volver = QPushButton("BACK TO MAINFRAME")
        boton_volver.clicked.connect(self.volver_callback)

        layout_principal.addWidget(boton_volver)

        self.setLayout(layout_principal)

    def crear_panel_lista(self):
        panel = QFrame()
        panel.setObjectName("Panel")

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(12)

        titulo = QLabel("SAVED NOTES")
        titulo.setObjectName("SectionTitle")

        self.lista_notas = QListWidget()
        self.lista_notas.itemClicked.connect(self.mostrar_nota_seleccionada)

        self.boton_eliminar = QPushButton("DELETE SELECTED")
        self.boton_eliminar.clicked.connect(self.eliminar_nota)

        layout.addWidget(titulo)
        layout.addWidget(self.lista_notas)
        layout.addWidget(self.boton_eliminar)

        panel.setLayout(layout)

        return panel

    def crear_panel_editor(self):
        panel = QFrame()
        panel.setObjectName("Panel")

        layout= QVBoxLayout()

        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(12)

        titulo = QLabel("NEW NOTE")
        titulo.setObjectName("SectionTitle")

        self.input_titulo = QLineEdit()
        self.input_titulo.setPlaceholderText("Note title")

        self.input_contenido = QTextEdit()
        self.input_contenido.setPlaceholderText("Wirte your note here...")

        self.boton_guardar = QPushButton("SAVE NOTE")
        self.boton_guardar.clicked.connect(self.guardar_nota)

        self.boton_limpiar = QPushButton("CLEAR")
        self.boton_limpiar.clicked.connect(self.limpiar_editor)

        layout.addWidget(titulo)
        layout.addWidget(self.input_titulo)
        layout.addWidget(self.input_contenido)
        layout.addWidget(self.boton_guardar)
        layout.addWidget(self.boton_limpiar)

        panel.setLayout(layout)

        return panel

    def cargar_lista_notas(self):
        self.lista_notas.clear()

        self.notas = self.notes_manager.cargar_notas()

        for nota in self.notas:
            texto = f"{nota["id"]} -{nota["titulo"]}"
            self.lista_notas.addItem(texto)

    def guardar_nota(self):
        titulo = self.input_titulo.text().strip()
        contenido = self.input_contenido.toPlainText().strip()

        if titulo == "" or contenido == "":
            QMessageBox.warning(
                self,
                "Missing data",
                "Please write a title and content before saving."
            )
            return 

        self.notes_manager.crear_nota(titulo,contenido)

        self.limpiar_editor()
        self.cargar_lista_notas()

    def mostrar_nota_seleccionada(self):
        fila = self.lista_notas.currentRow()

        if fila < 0:
            return 

        nota = self.notas[fila]

        self.input_titulo.setText(nota["titulo"])
        self.input_contenido.setText(nota["contenido"])

    def eliminar_nota(self):
        fila = self.lista_notas.currentRow()

        if fila < 0:
            QMessageBox.warning(
                self,
                "No note selected"
                "Please select a note before deleting.",
            )
            return 

        nota = self.notas[fila]
        id_nota = nota["id"]

        self.notes_manager.eliminar_nota(id_nota)

        self.limpiar_editor()
        self.cargar_lista_notas()

    def limpiar_editor(self):
        self.input_titulo.clear()
        self.input_contenido.clear()
        self.lista_notas.clearSelection()



    


