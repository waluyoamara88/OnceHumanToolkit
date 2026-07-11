import typer
from pathlib import Path
from generator.core.engine import GeneratorEngine
app=typer.Typer()
@app.command()
def build():
    GeneratorEngine(Path(__file__).resolve().parents[2]).run()
if __name__=="__main__": app()
