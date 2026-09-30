from fastapi import FastAPI

app = FastAPI(title="k8s-demo-api")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}