from pathlib import Path

class TemplateRenderer:

    def render(self,path,variables):

        text=Path(path).read_text(encoding="utf8")

        for k,v in variables.items():
            text=text.replace("{{ "+k+" }}",str(v))

        return text
