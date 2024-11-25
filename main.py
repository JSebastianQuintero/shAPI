from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# routes
from paths.houses import router as houseRouter
from paths.marketing import router as marketingRouter
from paths.clients import router as clientRouter

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app = FastAPI()

app.mount("/housePostImg", StaticFiles(directory="housePostImg"), name="housePostImg")

app.include_router(houseRouter)
app.include_router(marketingRouter)
app.include_router(clientRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
