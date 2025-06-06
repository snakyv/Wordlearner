import pyttsx3
import random
import json
import csv
import threading
from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import QPropertyAnimation, QRect
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_quizdialog import Ui_Dialog as Ui_QuizDialog
from models import WordRepository, StatsManager
from graph_window import GraphWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.repo = WordRepository()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._refresh_list()

        self.current_theme = "dark"
        self.current_style = self.load_style("styles/dark.qss")
        self.apply_styles(self.current_style)

        self.ui.importButton.setIcon(QIcon("icons/import.png"))
        self.ui.exportButton.setIcon(QIcon("icons/export.png"))
        self.ui.resetButton.setIcon(QIcon("icons/reset.png"))
        self.ui.quizButton.setIcon(QIcon("icons/start.png"))
        self.update_theme_icon()

        self.ui.importButton.clicked.connect(lambda: [self.animate_button(self.ui.importButton), self.open_import()])
        self.ui.quizButton.clicked.connect(lambda: [self.animate_button(self.ui.quizButton), self.start_quiz()])
        self.ui.resetButton.clicked.connect(lambda: [self.animate_button(self.ui.resetButton), self.reset_words()])
        self.ui.toggleThemeButton.clicked.connect(lambda: [self.animate_button(self.ui.toggleThemeButton), self.toggle_theme()])
        self.ui.exportButton.clicked.connect(lambda: [self.animate_button(self.ui.exportButton), self.export_words()])
        self.ui.addWordButton.clicked.connect(lambda: [self.animate_button(self.ui.addWordButton), self.add_word()])
        self.ui.editWordButton.clicked.connect(lambda: [self.animate_button(self.ui.editWordButton), self.edit_word()])
        self.ui.deleteWordButton.clicked.connect(lambda: [self.animate_button(self.ui.deleteWordButton), self.delete_word()])
        self.ui.showGraphButton.clicked.connect(lambda: [self.animate_button(self.ui.showGraphButton), self.show_graph()])

    def load_style(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            QMessageBox.warning(self, "Style Error", f"Failed to load style: {e}")
            return ""

    def apply_styles(self, style):
        self.setStyleSheet(style)

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_style = self.load_style("styles/light.qss")
            self.current_theme = "light"
        else:
            self.current_style = self.load_style("styles/dark.qss")
            self.current_theme = "dark"
        self.apply_styles(self.current_style)
        self.update_theme_icon()

    def update_theme_icon(self):
        icon_path = "icons/dark_mode.png" if self.current_theme == "dark" else "icons/light_mode.png"
        self.ui.toggleThemeButton.setIcon(QIcon(icon_path))

    def _refresh_list(self):
        self.ui.wordList.clear()
        for src, data in self.repo.words.items():
            mark = "⭐" if data.get("favorite") else ""
            self.ui.wordList.addItem(f"{mark}{src} – {data['translation']}")

    def open_import(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import Words", filter="JSON (*.json);;CSV (*.csv)")
        if path:
            try:
                self.repo.import_from_file(path)
                self._refresh_list()
                QMessageBox.information(self, "Success", "Words imported successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to import: {e}")

    def export_words(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Words", filter="JSON (*.json);;CSV (*.csv)")
        if path:
            try:
                if path.endswith(".json"):
                    with open(path, "w", encoding="utf-8") as f:
                        json.dump(self.repo.words, f, ensure_ascii=False, indent=2)
                elif path.endswith(".csv"):
                    with open(path, "w", newline='', encoding="utf-8") as f:
                        writer = csv.writer(f)
                        for src, data in self.repo.words.items():
                            writer.writerow([src, data["translation"]])
                QMessageBox.information(self, "Export", "Words exported successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export: {e}")

    def start_quiz(self):
        if not self.repo.words:
            QMessageBox.information(self, "Empty", "Please import words first")
            return

        mode, ok = QInputDialog.getItem(self, "Choose Mode",
                                        "Select quiz mode:",
                                        ["Direct (word → translation)",
                                         "Reverse (translation → word)",
                                         "Multiple choice"],
                                        0, False)
        if ok:
            dlg = QuizDialog(self.repo.words.copy(), mode, self.current_style)
            dlg.exec()

    def reset_words(self):
        confirm = QMessageBox.question(self, "Confirm Reset", "Are you sure you want to reset all words?")
        if confirm == QMessageBox.Yes:
            self.repo.words = {}
            self.repo.save()
            self._refresh_list()
            QMessageBox.information(self, "Reset", "All words have been cleared!")

    def add_word(self):
        src, ok1 = QInputDialog.getText(self, "Add Word", "Enter original word:")
        if not ok1 or not src:
            return
        trg, ok2 = QInputDialog.getText(self, "Add Word", "Enter translation:")
        if not ok2 or not trg:
            return
        self.repo.words[src] = {"translation": trg, "favorite": False}
        self.repo.save()
        self._refresh_list()
        QMessageBox.information(self, "Added", f"Word '{src}' added successfully!")

    def edit_word(self):
        item = self.ui.wordList.currentItem()
        if not item:
            QMessageBox.warning(self, "Select Word", "Please select a word to edit.")
            return
        src = item.text().split(" – ")[0].replace("⭐", "").strip()
        current_trg = self.repo.words[src]["translation"]
        new_trg, ok = QInputDialog.getText(self, "Edit Word", f"Edit translation for '{src}':", text=current_trg)
        if ok and new_trg:
            self.repo.words[src]["translation"] = new_trg
            self.repo.save()
            self._refresh_list()
            QMessageBox.information(self, "Edited", f"Word '{src}' updated!")

    def delete_word(self):
        item = self.ui.wordList.currentItem()
        if not item:
            QMessageBox.warning(self, "Select Word", "Please select a word to delete.")
            return
        src = item.text().split(" – ")[0].replace("⭐", "").strip()
        confirm = QMessageBox.question(self, "Confirm Delete", f"Delete word '{src}'?")
        if confirm == QMessageBox.Yes:
            del self.repo.words[src]
            self.repo.save()
            self._refresh_list()
            QMessageBox.information(self, "Deleted", f"Word '{src}' deleted!")

    def animate_button(self, button):
        rect = button.geometry()
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(150)
        animation.setStartValue(rect)
        animation.setEndValue(QRect(rect.x() - 4, rect.y() - 4, rect.width() + 8, rect.height() + 8))
        animation.setLoopCount(2)
        animation.setDirection(QPropertyAnimation.Backward)
        animation.start()
        self.animation = animation

    def show_graph(self):
        dlg = GraphWindow(self.current_style)
        dlg.exec()


class QuizDialog(QDialog):
    def __init__(self, words, mode, style):
        super().__init__()
        self.ui = Ui_QuizDialog()
        self.ui.setupUi(self)
        self.setStyleSheet(style)

        # Иконка на кнопку звука
        self.ui.soundButton.setIcon(QIcon("icons/sound_button.png"))
        self.ui.soundButton.setText("")

        self.words = list(words.items())
        self.total_questions = len(self.words)
        self.completed_questions = 0
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setTextVisible(True)

        self.current = None
        self.correct_count = 0
        self.total_count = 0
        self.mode = mode
        self.wrong_words = []

        self.ui.checkButton.clicked.connect(lambda: [self.animate_button(self.ui.checkButton), self.check_answer()])
        self.ui.nextButton.clicked.connect(lambda: [self.animate_button(self.ui.nextButton), self.next_word()])
        self.ui.soundButton.clicked.connect(lambda: [self.animate_button(self.ui.soundButton), self.play_word()])

        self.next_word()

    def next_word(self):
        if not self.words:
            QMessageBox.information(self, "Quiz Completed",
                                    f"Quiz finished!\nCorrect: {self.correct_count}/{self.total_count}")
            stats = StatsManager()
            stats.update(self.correct_count, self.total_count, self.wrong_words)
            self.ui.progressBar.setValue(100)
            self.accept()
            return

        self.current = random.choice(self.words)
        self.ui.answerEdit.clear()
        self.ui.resultLabel.clear()
        self.words.remove(self.current)

        if self.mode == "Direct (word → translation)":
            self.ui.wordLabel.setText(self.current[0])
        elif self.mode == "Reverse (translation → word)":
            self.ui.wordLabel.setText(self.current[1]["translation"])
        elif self.mode == "Multiple choice":
            self.ui.wordLabel.setText(self.current[0])

    def check_answer(self):
        user_input = self.ui.answerEdit.text().strip().lower()
        correct_answer = (self.current[1]["translation"] if self.mode != "Reverse (translation → word)" else self.current[0]).lower()
        self.total_count += 1

        if user_input == correct_answer:
            self.correct_count += 1
            self.ui.resultLabel.setText("✅ Вірно!")
        else:
            self.wrong_words.append(self.current[0])
            self.ui.resultLabel.setText(f"❌ Невірно! Правильно: {correct_answer}")

        self.completed_questions += 1
        progress = int((self.completed_questions / self.total_questions) * 100)
        self.ui.progressBar.setValue(progress)

    def play_word(self):
        def speak():
            local_engine = pyttsx3.init()
            local_engine.say(self.current[0])
            local_engine.runAndWait()
            local_engine.stop()

        threading.Thread(target=speak).start()

    def animate_button(self, button):
        rect = button.geometry()
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(150)
        animation.setStartValue(rect)
        animation.setEndValue(QRect(rect.x() - 4, rect.y() - 4, rect.width() + 8, rect.height() + 8))
        animation.setLoopCount(2)
        animation.setDirection(QPropertyAnimation.Backward)
        animation.start()
        if not hasattr(self, '_animations'):
            self._animations = []
        self._animations.append(animation)
        self._animations = [a for a in self._animations if a.state() != QPropertyAnimation.Stopped]
