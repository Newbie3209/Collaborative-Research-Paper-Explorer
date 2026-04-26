from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.chat_routes import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 🔥 important
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "API running 🚀"}
