from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from typing import Annotated
from pydantic import Field

# Define request schema: exactly 4 float values
class PredictRequest(BaseModel):
    features: Annotated[list[float], Field(min_length=4, max_length=4)]

# Define response schema
class PredictResponse(BaseModel):
    prediction: Literal["class A", "class B", "class C", "class D"]

app = FastAPI()

# Dummy rule-based classifier, Business Logic
def dummy_classifier(features):
    if features[0] < 1.0:
        return "class A"
    elif features[0] < 2.0:
        return "class B"
    elif features[0] < 3.0:
        return "class C"
    else:
        return "class D"

# Prediction endpoint
@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = dummy_classifier(request.features)
    return {"prediction": prediction}