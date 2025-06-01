import matplotlib.pyplot as plt
from datetime import datetime
from PySide6.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from models import StatsManager

class GraphWindow(QDialog):
    def __init__(self, style):
        super().__init__()
        self.setWindowTitle("Progress Graph")
        self.setMinimumSize(700, 500)
        self.setStyleSheet(style)

        layout = QVBoxLayout(self)

        stats = StatsManager()
        history = stats.stats.get("history", [])
        if not history:
            return

        try:
            dates = [datetime.strptime(record["date"], "%Y-%m-%d %H:%M") for record in history]
        except ValueError:
            dates = []
        scores = [record["score"] for record in history]

        if not dates or not scores:
            return

        fig, ax = plt.subplots()
        ax.plot(dates, scores, marker='o', linestyle='-', color='skyblue')
        ax.set_title("Progress Over Time")
        ax.set_xlabel("Date & Time")
        ax.set_ylabel("Score (%)")
        ax.set_ylim(0, 100)

        fig.autofmt_xdate(rotation=45)

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
