import json
import datetime
from pathlib import Path

class WordRepository:
    def __init__(self, path="data/words.json"):
        self.path = Path(path)
        self.words = self._load()

    def _load(self):
        if not self.path.exists():
            return {}
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            updated = {}
            for k, v in raw.items():
                if isinstance(v, str):
                    updated[k] = {"translation": v, "favorite": False}
                else:
                    updated[k] = v
            return updated
        except json.JSONDecodeError:
            return {}

    def save(self):
        self.path.parent.mkdir(exist_ok=True)
        self.path.write_text(json.dumps(self.words, ensure_ascii=False, indent=2), encoding="utf-8")

    def import_from_file(self, filepath):
        ext = Path(filepath).suffix.lower()
        data = {}
        if ext == ".json":
            raw = json.loads(Path(filepath).read_text(encoding="utf-8"))
            for k, v in raw.items():
                if isinstance(v, str):
                    data[k] = {"translation": v, "favorite": False}
                else:
                    data[k] = v
        elif ext == ".csv":
            import csv
            with open(filepath, newline='', encoding="utf-8") as f:
                for src, trg in csv.reader(f):
                    data[src] = {"translation": trg, "favorite": False}
        else:
            raise ValueError("Unsupported format")
        self.words.update(data)
        self.save()

    def mark_favorite(self, word):
        if word in self.words:
            self.words[word]["favorite"] = True
            self.save()

    def unmark_favorite(self, word):
        if word in self.words:
            self.words[word]["favorite"] = False
            self.save()


class StatsManager:
    def __init__(self, path="data/stats.json"):
        self.path = Path(path)
        self.stats = self._load()

    def _load(self):
        if not self.path.exists():
            return {"total_tests": 0, "average_score": 0, "hard_words": {}, "history": []}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self):
        self.path.write_text(json.dumps(self.stats, ensure_ascii=False, indent=2), encoding="utf-8")

    def update(self, correct, total, wrong_words):
        self.stats["total_tests"] += 1
        current_score = (correct / total) * 100 if total else 0
        prev_avg = self.stats["average_score"]
        total_tests = self.stats["total_tests"]
        self.stats["average_score"] = ((prev_avg * (total_tests - 1)) + current_score) / total_tests

        for word in wrong_words:
            self.stats["hard_words"][word] = self.stats["hard_words"].get(word, 0) + 1

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.stats.setdefault("history", []).append({
            "date": now,
            "score": round(current_score, 2)
        })

        self.save()
