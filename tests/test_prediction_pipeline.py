import pandas as pd

from src.pipeline.prediction_pipeline import CustomData, PredictPipeline


def test_prediction_pipeline_initialization():
    pipeline = PredictPipeline()

    assert pipeline.model is not None
    assert pipeline.preprocessor is not None


def test_custom_data_to_dataframe():
    data = CustomData(
        Company="Dell",
        Product="Inspiron 15",
        TypeName="Notebook",
        Inches=15.6,
        Ram=8,
        OS="Windows 10",
        Weight=2.1,
        Screen="Full HD",
        ScreenW=1920,
        ScreenH=1080,
        Touchscreen=0,
        IPSpanel=1,
        RetinaDisplay=0,
        CPU_company="Intel",
        CPU_freq=2.5,
        CPU_model="Core i5",
        PrimaryStorage=256,
        SecondaryStorage=0,
        PrimaryStorageType="SSD",
        SecondaryStorageType="None",
        GPU_company="Intel",
        GPU_model="HD Graphics 620",
    )

    df = data.get_data_as_dataframe()

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 22)


def test_prediction_pipeline():
    data = CustomData(
        Company="Dell",
        Product="Inspiron 15",
        TypeName="Notebook",
        Inches=15.6,
        Ram=8,
        OS="Windows 10",
        Weight=2.1,
        Screen="Full HD",
        ScreenW=1920,
        ScreenH=1080,
        Touchscreen=0,
        IPSpanel=1,
        RetinaDisplay=0,
        CPU_company="Intel",
        CPU_freq=2.5,
        CPU_model="Core i5",
        PrimaryStorage=256,
        SecondaryStorage=0,
        PrimaryStorageType="SSD",
        SecondaryStorageType="None",
        GPU_company="Intel",
        GPU_model="HD Graphics 620",
    )

    df = data.get_data_as_dataframe()

    pipeline = PredictPipeline()

    prediction = pipeline.predict(df)

    assert prediction is not None
    assert len(prediction) == 1
