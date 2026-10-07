from fastapi import FastAPI

app=FastAPI(
    title="AI Learning Platform",
    description="AI powered learning resource and tuterial platform",
    version="0.1.0"

)

@app.get("/")
def root():
    return{
        "Message":"AI Learning Platform"
    }



