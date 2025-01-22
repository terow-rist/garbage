# BMI Calculator API

This is a simple API built using FastAPI to calculate Body Mass Index (BMI) based on a person's height and weight. The API also classifies the BMI into categories such as underweight, normal weight, overweight, or obesity.

## Features
- Accepts height (in meters) and weight (in kilograms) as input.
- Validates the input values for correctness.
- Calculates BMI using the formula:
  
  \[
  BMI = \frac{\text{weight (kg)}}{\text{height (m)}^2}
  \]

- Returns the calculated BMI rounded to two decimal places.
- Provides a classification of the BMI into one of the following categories:
  - Underweight
  - Normal weight
  - Overweight
  - Obesity

## Installation


1. **Create and activate a virtual environment:**
   ```bash
   pythonX -m venv .venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI server:**
   ```bash
   fastapi dev main.py
   ```

   Replace `main` with the name of your Python file if it differs.

2. **Access the API documentation:**
   - Open your browser and navigate to:
     - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. **Make a POST request to the `/calculate_bmi` endpoint:**
   - **Endpoint:** `/calculate_bmi`
   - **Method:** POST
   - **Request Body:**
     ```json
     {
       "height": 1.75,
       "weight": 70
     }
     ```

   - **Response:**
     ```json
     {
       "bmi": 22.86,
       "classification": "Normal weight"
     }
     ```

## Input Validation
- `height` must be a positive value greater than 0.
- `weight` must be a positive value greater than 0.

## Example Response
### Valid Input:
**Request Body:**
```json
{
  "height": 1.75,
  "weight": 70
}
```
**Response:**
```json
{
  "bmi": 22.86,
  "classification": "Normal weight"
}
```

### Invalid Input:
**Request Body:**
```json
{
  "height": 0,
  "weight": 70
}
```
**Response:**
```json
{
  "error": "Height must be greater than zero."
}
```

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any feature requests or bug fixes.

## Contact
For questions or feedback, please contact [feeerhd.342@gmail.com].

