from pathlib import Path

class FileSystem:

    @staticmethod
    def mkdir(path):
        Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def write(path, text):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
