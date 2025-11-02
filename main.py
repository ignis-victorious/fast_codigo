# 
#  Import LIBRARIES
from fastapi import FastAPI
import uvicorn
#  Import FILES
#  ...

app = FastAPI(title="Mi Primera API", description="Aprendiendo FastAPI", version="0.1.0")

@app.get("/")
async def root() :
    return {"message": "¡Hola, FastAPI!"}


# Para ejecutar: uvicorn main:app --reload


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# 
#  Import LIBRARIES
#  Import FILES
#  ...