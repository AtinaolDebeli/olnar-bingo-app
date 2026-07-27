from fastapi import FastAPI

app = FastAPI(
    title="Olnar Bingo API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "project": "Olnar Bingo",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }
