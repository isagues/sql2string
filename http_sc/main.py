from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/{sc}")
async def read_item(sc: int):
    return Response(content=None, status_code=sc)