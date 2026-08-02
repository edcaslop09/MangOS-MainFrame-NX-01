from PySide6.QtWidgets import QMainWindow, QStackedWidget

from gui.pages.dashboard_page import DashboardPage
from gui.pages.simple_page import SimplePage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MangOS MainFrame NX-01")
        self.setMinimumSize(1000,650)

        self.paginas = QStackedWidget()

        self.dashboard = DashboardPage(
            abrir_static_records = self.mostrar_static_records,
            abrir_vinyl_black = self.mostrar_vinyl_black,
            abrir_notes = self.mostrar_notes,
            abrir_status = self.mostrar_status,
            abrir_settings = self.mostrar_settings,
            cerrar_app = self.close,
        )

        self.static_records_page = SimplePage(
            titulo = "STATIC RECORDS",
            subtitulo = "Local FLAC Music Workstation",
            descripcion=(
                "Static Records is the local music app inside MangOS."
                "This screen will connect to the existing music library,"
                "playback engine, playlists, lyrics system and audio filters."
            ),
            volver_callback= self.mostrar_dashboard,
        )

        self.vinyl_black_oage = SimplePage(
            titulo = "VINYL BLACK.FM",
            subtitulo = "Local Virtual Radio Station",
            descripcion= (
                "Vinyl Black.FM is a local radio mode powered by STATIC RECORDS."
                "This screen will control radio playback, filters, mute mode and "
                "station status."
            ),
            volver_callback= self.mostrar_dashboard,
        )

        self.notes_page = SimplePage(
            titulo = "NOTES",
            subtitulo = "Local Notes App",
            descripcion=(
                "Notes will be a simple local-first app for writting, saving, "
                "reading and deleting notes inside MangOS."
            ),
            volver_callback= self.mostrar_dashboard,
        )

        self.status_page = SimplePage(
                    titulo = "SYSTEM STATUS",
                    subtitulo = "MangOS Runtime Information",
                    descripcion=(
                        "System Status will display boot mode, available apps, local data "
                        "paths, Static Records library status, playlist count and general "
                        "runtime information. "
                    ),
                    volver_callback= self.mostrar_dashboard,
                )
        
        self.settings_page = SimplePage(
                    titulo = "SETTINGS",
                    subtitulo = "System Configuration",
                    descripcion=(
                        "Settings will later control MangOS preferences, visual options, "
                        "startup behavior and app configuration."
                    ),
                    volver_callback= self.mostrar_dashboard,
                )

        self.paginas.addWidget(self.dashboard)
        self.paginas.addWidget(self.static_records_page)
        self.paginas.addWidget(self.vinyl_black_oage)
        self.paginas.addWidget(self.notes_page)
        self.paginas.addWidget(self.status_page)
        self.paginas.addWidget(self.settings_page)

        self.setCentralWidget(self.paginas)

    def mostrar_dashboard(self):
        self.paginas.setCurrentWidget(self.dashboard)

    def mostrar_static_records(self):
        self.paginas.setCurrentWidget(self.static_records_page)

    def mostrar_vinyl_black(self):
        self.paginas.setCurrentWidget(self.vinyl_black_oage)

    def mostrar_notes(self):
        self.paginas.setCurrentWidget(self.notes_page)

    def mostrar_status(self):
        self.paginas.setCurrentWidget(self.status_page)

    def mostrar_settings(self):
        self.paginas.setCurrentWidget(self.settings_page)
    



