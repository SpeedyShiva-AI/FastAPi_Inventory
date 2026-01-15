from fastapi import FastAPI

app=FastAPI(title="Inventory and Reorder API")

@app.get("/")
def root():
    return{"message":"inventory api is running"}

@app.get("/health")
def health_check():
    return{"status":"ok"}