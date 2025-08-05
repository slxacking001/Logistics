#Import system modules here
import uvicorn
from fastapi import FastAPI

# Import Personal modules here
from app.routes import api_routes

# Declare Instances her
app = FastAPI()

# This includes routes from app.routes
app.include_router(api_routes)

# This is root route
@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

global func 
func = root()

@app.get("/answertoquestionis")
def room():
    x = 8 + 4
    y = 16 + 17
    root = func
    return {"x": x, "y":y, "root": root}

# This auto starts your API server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)