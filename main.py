from fastapi import FastAPI # type: ignore
app = FastAPI()

@app.get("/welcome")
def welcome():
    return{
        "message" : "hi!"
    }
