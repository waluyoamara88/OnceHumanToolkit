from fastapi import FastAPI
app=FastAPI(title='OnceHumanToolkit')
@app.get('/')
def root():
    return {'status':'ok'}
