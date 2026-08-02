
def get_stylesheet():
    return """
    QWidget {
    backrgound-color: #050505;
    color: #F6C85F;
    font-family: Consolas, "Courier New", monospace;
    font-size 14px;
    }

    QMainWindow {
        background-color: #050505;
    }

    QLabel#TitleLabel {
        color: #FFD166;
        font-size: 30px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    QLabel#SubtitleLabel {
        color: #F77F00;
        font-size: 15px;
    }

    QLabel#SectionTitle {
        color: #FFD166;
        font-size: 18px;
        font-weight: bold;
    }
    
    QLabel#StatusText {
        color: #EAE2B7;
        font-size: 14px;
    }

    QFrame#Panel {
        background-color: #111111;
        border: 1px solid #F77F00;
        border-radius: 10px;
    }

    QPushButton {
        backrground-color: #151515;
        color: #FFD166;
        border: 1px solid #F77F00;
        border-radius: 8px;
        padding: 12px<;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #2A1800,
        border: 1px solid #FFD166;
    }

    QPushButton:pressed {
        backrground-color: #F77F00;
        color: #050505;
    }
    """