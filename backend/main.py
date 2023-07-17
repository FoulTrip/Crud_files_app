from fastapi import FastAPI
from routes.files import files
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuro los orígenes permitidos (origins) en el CORS Middleware
origins = [
    "http://localhost:5173", # URL del frontend y se puede agregar mas
    # "http://randomPage:5000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files)


