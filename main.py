#
#  Import LIBRARIES
import uvicorn
from fastapi import FastAPI

#  Import FILES
#  ...

app = FastAPI(title="Mi Primera API", description="Aprendiendo FastAPI", version="0.1.0")


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


# Para ejecutar: uvicorn main:app --reload .... Old way!
if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)


#
#  Import LIBRARIES
#  Import FILES
#  ...
