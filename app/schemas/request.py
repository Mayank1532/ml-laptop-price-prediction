from pydantic import BaseModel


class PredictionRequest(BaseModel):
    Company: str
    Product: str
    TypeName: str
    Inches: float
    Ram: int
    OS: str
    Weight: float
    Screen: str
    ScreenW: int
    ScreenH: int
    Touchscreen: int
    IPSpanel: int
    RetinaDisplay: int
    CPU_company: str
    CPU_freq: float
    CPU_model: str
    PrimaryStorage: int
    SecondaryStorage: int
    PrimaryStorageType: str
    SecondaryStorageType: str
    GPU_company: str
    GPU_model: str
