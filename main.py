from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# routes
from paths.houses import router as houseRouter
from paths.marketing import router as marketingRouter
from paths.clients import router as clientRouter

app = FastAPI()

app.mount("/housePostImg", StaticFiles(directory="housePostImg"), name="housePostImg")

app.include_router(houseRouter)
app.include_router(marketingRouter)
app.include_router(clientRouter)
