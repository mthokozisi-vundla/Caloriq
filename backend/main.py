from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.database import connection

class Food(BaseModel):
    name: str
    calories: int
    protein: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Caloriq!"}

@app.get("/hello")
def hello():
    return {"message": "Hello from Caloriq!"}

@app.get("/about")
def about():
    return {"message": "Caloriq is a nutrition tracking application."}

@app.get("/foods")
def get_foods():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM foods")
    foods = cursor.fetchall()


    return[
        {                       #type: ignore
            "id": food[0],
            "name": food[1],
            "calories": food[2],
            "protein": float(food[3])
        }
        for food in foods
    ]

@app.post("/foods")
def create_food(food: Food):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO foods (name, calories, protein) VALUES (%s, %s, %s)",
        (food.name, food.calories, food.protein)
    )

    connection.commit()

    food_id = cursor.lastrowid

    return {          #type: ignore
    "id": food_id,
    "name": food.name,
    "calories": food.calories,
    "protein": food.protein
}

@app.get("/foods/{food_id}")
def get_food(food_id: int):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM foods WHERE id = %s",
        (food_id,)
    )

    food = cursor.fetchone()

    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")

    return {        #type: ignore
        "id": food[0],
        "name": food[1],
        "calories": food[2],
        "protein": float(food[3])
    }

