from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.database import connection

class Food(BaseModel):
    name: str
    calories: int
    protein: float

class User(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    goal: str

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

    return {          #type: ignore
        "id": food[0],
        "name": food[1],
        "calories": food[2],
        "protein": float(food[3])
    }

@app.put("/foods/{food_id}")
def update_food(food_id: int, food: Food):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM foods WHERE id = %s",
        (food_id,)
    )

    existing_food = cursor.fetchone()

    if existing_food is None:
        raise HTTPException(status_code=404, detail="Food not found")

    cursor.execute(
        """
        UPDATE foods
        SET name = %s, calories = %s, protein = %s
        WHERE id = %s
        """,
        (food.name, food.calories, food.protein, food_id)
    )

    connection.commit()

    return {          #type: ignore
        "id": food_id,
        "name": food.name,
        "calories": food.calories,
        "protein": food.protein
    }

@app.delete("/foods/{food_id}")
def delete_food(food_id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM foods WHERE id = %s",
        (food_id,)
    )

    food = cursor.fetchone()

    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")

    cursor.execute(
        "DELETE FROM foods WHERE id = %s",
        (food_id,)
    )

    connection.commit()

    return {          #type: ignore
        "message": "Food deleted successfully",
        "id": food_id
    }

@app.post("/users")
def create_user(user: User):

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, age, height, weight, goal)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            user.name,
            user.age,
            user.height,
            user.weight,
            user.goal
        )
    )

    connection.commit()

    user_id = cursor.lastrowid

    return { #type: ignore
        "id": user_id,
        "name": user.name,
        "age": user.age,
        "height": user.height,
        "weight": user.weight,
        "goal": user.goal
    }
@app.get("/users")
def get_users():

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    return [
        { #type: ignore
            "id": user[0],
            "name": user[1],
            "age": user[2],
            "height": float(user[3]),
            "weight": float(user[4]),
            "goal": user[5]
        }
        for user in users
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return { #type: ignore
        "id": user[0],
        "name": user[1],
        "age": user[2],
        "height": float(user[3]),
        "weight": float(user[4]),
        "goal": user[5]
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    existing_user = cursor.fetchone()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    cursor.execute(
        """
        UPDATE users
        SET name = %s, age = %s, height = %s, weight = %s, goal = %s
        WHERE id = %s
        """,
        (
            user.name,
            user.age,
            user.height,
            user.weight,
            user.goal,
            user_id
        )
    )

    connection.commit()

    return {        #type: ignore
        "id": user_id,
        "name": user.name,
        "age": user.age,
        "height": user.height,
        "weight": user.weight,
        "goal": user.goal
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    cursor.execute(
        "DELETE FROM users WHERE id = %s",
        (user_id,)
    )

    connection.commit()

    return {        #type: ignore
        "message": "User deleted successfully",
        "id": user_id
    }