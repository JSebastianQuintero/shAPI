from fastapi import FastAPI

# routes
from paths.houses import router as houseRouter
from paths.marketing import router as marketingRouter
from paths.clients import router as clientRouter

app = FastAPI()

app.include_router(houseRouter)
app.include_router(marketingRouter)
app.include_router(clientRouter)
