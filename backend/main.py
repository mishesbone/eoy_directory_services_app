from fastapi import FastAPI, Depends
from backend.config.db_config import Base, engine
from backend.api.routes import user_management, login

app = FastAPI(title="eOY Directory Services")

# Initialize database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_management.router, prefix="/users", tags=["User Management"])
app.include_router(login.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to eOY Directory Services"}
