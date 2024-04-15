import time
from PyQt5.QtWidgets import QApplication, QWidget, QRubberBand, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect
class ScreenCapture(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setMouseTracking(True)
        self.origin = None
        self.end = None
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.captureScreen()
    def captureScreen(self):
        try:
            time.sleep(0.31)  # A small delay to ensure screen is captured properly
            screen = QApplication.primaryScreen()
            screenshot = screen.grabWindow(0)
            self.screenshot = screenshot.toImage()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.close()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.screenshot)
        if self.origin and self.end:
            rect = QRect(self.origin, self.end).normalized()
            painter.setBrush(Qt.NoBrush)
            painter.drawRect(rect)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.end = event.pos()
            self.update()
    def mouseMoveEvent(self, event):
        if self.origin:
            self.end = event.pos()
            self.update()
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.origin:
            self.end = event.pos()
            rect = QRect(self.origin, self.end).normalized()
            region = self.screenshot.copy(rect)
            region.save("screenshot.png")
            self.close()
def capture_screen():
    app = QApplication([])
    window = ScreenCapture()
    window.show()
    app.exec_()



