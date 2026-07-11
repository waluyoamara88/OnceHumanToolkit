from pathlib import Path

root = Path(__file__).resolve().parent.parent

files = {
"README.md":"# OnceHumanToolkit\n",
".gitignore":"__pycache__/\n.venv/\nnode_modules/\n",
"requirements.txt":"fastapi\nuvicorn\n",
"pyproject.toml":"""[project]
name="oncehumantoolkit"
version="0.1.0"
requires-python=">=3.14"
""",
"backend/app/main.py":"""from fastapi import FastAPI
app=FastAPI(title='OnceHumanToolkit')
@app.get('/')
def root():
    return {'status':'ok'}
""",
"data/json/.gitkeep":"",
"database/sqlite/.gitkeep":"",
}

for rel,content in files.items():
    p=root/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")

print("Generator V1 completed.")
