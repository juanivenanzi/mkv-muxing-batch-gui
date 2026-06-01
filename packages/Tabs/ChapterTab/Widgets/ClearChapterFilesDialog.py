from packages.Startup import GlobalIcons
from packages.Widgets.YesNoDialog import YesNoDialog


class ClearChapterFilesDialog(YesNoDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.message.setText(
            "¿Está seguro?\nEsto borrará todos los archivos de capítulos"
        )
        self.setWindowTitle("Borrar Archivos de Capítulos")
        self.setWindowIcon(GlobalIcons.NoMarkIcon)

    def execute(self):
        self.exec()
