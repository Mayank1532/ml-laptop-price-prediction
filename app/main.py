from fastapi import FastAPI

from app.routers.prediction import router as prediction_router

app = FastAPI(
    title="Laptop Price Prediction API",
    description="Predict laptop prices using a trained ML model.",
    version="1.0.0",
)

app.include_router(prediction_router)


@app.get("/")
def root():
    return {"message": "Laptop Price Prediction API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
