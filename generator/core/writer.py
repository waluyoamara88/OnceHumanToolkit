from pathlib import Path

class ProjectWriter:

    @staticmethod
    def write(path, content):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
