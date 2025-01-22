from fastapi import FastAPI
from pydantic import BaseModel


class BMIStruct(BaseModel):
    height: float  # Height in meters
    weight: float  # Weight in kilograms


app = FastAPI()

@app.post("/calculate_bmi")
async def calculate_bmi(data: BMIStruct):
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    """
    if data.height <= 0:
        return {"error": "Height must be greater than zero."}
    elif data.weight <= 0:
        return {"error": "Weight must be greater than zero."}

    bmi = data.weight / (data.height ** 2)

    classification = ""
    if bmi < 18.5:
        classification = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        classification = "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"
    
    return {
        "bmi": round(bmi, 2),
        "classification": classification
        }

