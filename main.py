from fastapi import FastAPI

app = FastAPI()


# Defines API route
@app.get("/api/v1/hello")
async def api():
    return {"message": "Hello World"}


# Defines root route to UI
@app.get("/")
async def root():
    return {"message": "Welcome to the UI (more functionality to come"}
