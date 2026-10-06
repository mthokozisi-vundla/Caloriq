import pymysql
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.database import get_connection

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
    sex: str
    activity_level: str

class FoodEntry(BaseModel):
    user_id: int
    food_id: int
    quantity: int
    meal: str
    entry_date: str | None = None

class WeightEntry(BaseModel):
    user_id: int
    weight: float
    entry_date: str | None = None

class Note(BaseModel):
    user_id: int
    content: str
    date: str | None = None

app = FastAPI()

ACTIVITY_FACTORS = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725,
    "extra active": 1.9
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    connection = get_connection()
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
    connection = get_connection()
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
    connection = get_connection()
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

    connection = get_connection()
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

    connection = get_connection()
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

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, age, sex, height, weight, activity_level, goal)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            user.name,
            user.age,
            user.sex,
            user.height,
            user.weight,
            user.activity_level,
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
        "goal": user.goal,
        "sex": user.sex,
        "activity_level": user.activity_level
    }

@app.get("/users")
def get_users():
    connection = get_connection()
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
            "goal": user[5],
            "sex": user[6],
            "activity_level": user[7]
        }
        for user in users
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):

    connection = get_connection()
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
        "goal": user[5],
        "sex": user[6],
        "activity_level": user[7]
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
        SET name = %s,
          age = %s, 
          height = %s, 
          weight = %s, 
          goal = %s, 
          sex = %s, 
          activity_level = %s
        WHERE id = %s
        """,
        (
            user.name,
            user.age,
            user.height,
            user.weight,
            user.goal,
            user.sex,
            user.activity_level,
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
        "goal": user.goal,
        "sex": user.sex,
        "activity_level": user.activity_level
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

@app.get("/users/{user_id}/calorie-target")
def get_calorie_target(user_id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    weight = float(user[4])
    height = float(user[3])
    age = user[2]
    sex = user[6]
    activity_level = user[7]
    goal = user[5]

    if sex == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_factor = ACTIVITY_FACTORS.get(activity_level)

    if activity_factor is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid activity level"
        )

    tdee = bmr * activity_factor

    if goal == "weight loss":
        calorie_target = tdee - 500
    elif goal == "weight gain":
        calorie_target = tdee + 300
    else:
        calorie_target = tdee

    return { #type: ignore
        "user_id": user_id,
        "bmr": round(bmr),
        "tdee": round(tdee),
        "goal": goal,
        "daily_calorie_target": round(calorie_target)
    }

@app.post("/food-entries")
def create_food_entry(entry: FoodEntry):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (entry.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Check that the food exists
    cursor.execute(
        "SELECT * FROM foods WHERE id = %s",
        (entry.food_id,)
    )

    food = cursor.fetchone()

    if food is None:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    # Make sure quantity is greater than 0
    if entry.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )
    if entry.entry_date is None:
        from datetime import date
        entry.entry_date = str(date.today())
    
    # Save the food entry
    cursor.execute(
        """
        INSERT INTO food_entries
        (user_id, food_id, quantity, meal, entry_date)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            entry.user_id,
            entry.food_id,
            entry.quantity,
            entry.meal,
            entry.entry_date
        )
    )

    connection.commit()

    entry_id = cursor.lastrowid

    return { # type: ignore
        "id": entry_id,
        "user_id": entry.user_id,
        "food_id": entry.food_id,
        "quantity": entry.quantity,
        "meal": entry.meal,
        "entry_date": entry.entry_date
    }

@app.get("/users/{user_id}/food-entries")
def get_food_entries(user_id: int):

    connection = get_connection()

    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get food entries and their food information
    cursor.execute(
        """
        SELECT
            food_entries.id,
            food_entries.user_id,
            food_entries.food_id,
            foods.name,
            foods.calories,
            foods.protein,
            food_entries.quantity,
            food_entries.meal,
            food_entries.entry_date
        FROM food_entries
        JOIN foods
            ON food_entries.food_id = foods.id
        WHERE food_entries.user_id = %s
        """,
        (user_id,)
    )

    entries = cursor.fetchall()

    cursor.close()
    connection.close()

    return [        #type: ignore
        {
            "id": entry["id"],
            "user_id": entry["user_id"],
            "food_id": entry["food_id"],
            "food_name": entry["name"],
            "calories_per_unit": entry["calories"],
            "protein_per_unit": float(entry["protein"]),
            "quantity": entry["quantity"],
            "meal": entry["meal"],
            "entry_date": str(entry["entry_date"]),
            "total_calories": entry["calories"] * entry["quantity"],
            "total_protein": float(entry["protein"]) * entry["quantity"]
        }
        for entry in entries
    ]

@app.get("/users/{user_id}/daily-summary")
def get_daily_summary(user_id: int):

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get today's date
    cursor.execute(
        """
        SELECT
            COALESCE(SUM(food_entries.quantity * foods.calories), 0),
            COALESCE(SUM(food_entries.quantity * foods.protein), 0)
        FROM food_entries
        JOIN foods
            ON food_entries.food_id = foods.id
        WHERE food_entries.user_id = %s
        AND food_entries.entry_date = CURDATE()
        """,
        (user_id,)
    )

    totals = cursor.fetchone()

    calories_consumed = totals[0]
    protein_consumed = totals[1]

    # Get the user's daily calorie target
    weight = float(user[4])
    height = float(user[3])
    age = user[2]
    sex = user[6]
    activity_level = user[7]
    goal = user[5]

    if sex == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_factor = ACTIVITY_FACTORS.get(activity_level)

    if activity_factor is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid activity level"
        )

    tdee = bmr * activity_factor

    if goal == "weight loss":
        calorie_target = tdee - 500
    elif goal == "weight gain":
        calorie_target = tdee + 300
    else:
        calorie_target = tdee

    daily_calorie_target = round(calorie_target)
    calories_remaining = daily_calorie_target - calories_consumed

    return {        #type: ignore
        "user_id": user_id,
        "date": str(__import__("datetime").date.today()),
        "daily_calorie_target": daily_calorie_target,
        "calories_consumed": calories_consumed,
        "calories_remaining": calories_remaining,
        "protein_consumed": float(protein_consumed)
    }


@app.delete("/food-entries/{entry_id}")
def delete_food_entry(entry_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the food entry exists
    cursor.execute(
        "SELECT * FROM food_entries WHERE id = %s",
        (entry_id,)
    )

    entry = cursor.fetchone()

    if entry is None:
        raise HTTPException(
            status_code=404,
            detail="Food entry not found"
        )

    # Delete the food entry
    cursor.execute(
        "DELETE FROM food_entries WHERE id = %s",
        (entry_id,)
    )

    connection.commit()

    return {       #type: ignore
        "message": "Food entry deleted successfully",
        "id": entry_id
    }

@app.put("/food-entries/{entry_id}")
def update_food_entry(entry_id: int, entry: FoodEntry):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the food entry exists
    cursor.execute(
        "SELECT * FROM food_entries WHERE id = %s",
        (entry_id,)
    )

    existing_entry = cursor.fetchone()

    if existing_entry is None:
        raise HTTPException(
            status_code=404,
            detail="Food entry not found"
        )

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (entry.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Check that the food exists
    cursor.execute(
        "SELECT * FROM foods WHERE id = %s",
        (entry.food_id,)
    )

    food = cursor.fetchone()

    if food is None:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    # Make sure quantity is greater than 0
    if entry.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )

    # Update the food entry
    cursor.execute(
        """
        UPDATE food_entries
        SET user_id = %s,
            food_id = %s,
            quantity = %s,
            meal = %s,
            entry_date = %s
        WHERE id = %s
        """,
        (
            entry.user_id,
            entry.food_id,
            entry.quantity,
            entry.meal,
            entry.entry_date,
            entry_id
        )
    )

    connection.commit()

    return {       #type: ignore
        "message": "Food entry updated successfully",
        "id": entry_id,
        "user_id": entry.user_id,
        "food_id": entry.food_id,
        "quantity": entry.quantity,
        "meal": entry.meal,
        "entry_date": entry.entry_date
    }

@app.post("/weight-entries")
def create_weight_entry(entry: WeightEntry):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (entry.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Make sure weight is greater than 0
    if entry.weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than 0"
        )

    # Save the weight entry
    cursor.execute(
        """
        INSERT INTO weight_entries
        (user_id, weight, date)
        VALUES (%s, %s, %s)
        """,
        (
            entry.user_id,
            entry.weight,
            entry.entry_date
        )
    )

    connection.commit()

    entry_id = cursor.lastrowid

    return {   #type: ignore
        "id": entry_id,
        "user_id": entry.user_id,
        "weight": entry.weight,
        "entry_date": entry.entry_date
    }

@app.get("/users/{user_id}/weight-entries")
def get_weight_entries(user_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get the user's weight history
    cursor.execute(
        """
        SELECT
            id,
            user_id,
            weight,
            date
        FROM weight_entries
        WHERE user_id = %s
        ORDER BY date DESC
        """,
        (user_id,)
    )

    entries = cursor.fetchall()

    return [     #type: ignore
        {
            "id": entry[0],
            "user_id": entry[1],
            "weight": float(entry[2]),
            "date": str(entry[3])
        }
        for entry in entries
    ]

@app.get("/users/{user_id}/weight-summary")
def get_weight_summary(user_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get the first recorded weight
    cursor.execute(
        """
        SELECT weight
        FROM weight_entries
        WHERE user_id = %s
        ORDER BY date ASC, id ASC
        LIMIT 1
        """,
        (user_id,)
    )

    first_entry = cursor.fetchone()

    # Get the most recent recorded weight
    cursor.execute(
        """
        SELECT weight
        FROM weight_entries
        WHERE user_id = %s
        ORDER BY date DESC, id DESC
        LIMIT 1
        """,
        (user_id,)
    )

    latest_entry = cursor.fetchone()

    # No weight records yet
    if first_entry is None or latest_entry is None:
        return {     #type: ignore
            "user_id": user_id,
            "starting_weight": None,
            "current_weight": None,
            "weight_change": None
        }

    starting_weight = float(first_entry[0])
    current_weight = float(latest_entry[0])

    weight_change = current_weight - starting_weight

    return {    #type: ignore
        "user_id": user_id,
        "starting_weight": starting_weight,
        "current_weight": current_weight,
        "weight_change": weight_change
    }

@app.put("/weight-entries/{entry_id}")
def update_weight_entry(entry_id: int, entry: WeightEntry):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the weight entry exists
    cursor.execute(
        "SELECT * FROM weight_entries WHERE id = %s",
        (entry_id,)
    )

    existing_entry = cursor.fetchone()

    if existing_entry is None:
        raise HTTPException(
            status_code=404,
            detail="Weight entry not found"
        )

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (entry.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Make sure weight is greater than 0
    if entry.weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than 0"
        )

    # Update the weight entry
    cursor.execute(
        """
        UPDATE weight_entries
        SET user_id = %s,
            weight = %s,
            date = %s
        WHERE id = %s
        """,
        (
            entry.user_id,
            entry.weight,
            entry.entry_date,
            entry_id
        )
    )

    connection.commit()

    return {      #type: ignore
        "message": "Weight entry updated successfully",
        "id": entry_id,
        "user_id": entry.user_id,
        "weight": entry.weight,
        "entry_date": entry.entry_date
    }

@app.delete("/weight-entries/{entry_id}")
def delete_weight_entry(entry_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the weight entry exists
    cursor.execute(
        "SELECT * FROM weight_entries WHERE id = %s",
        (entry_id,)
    )

    entry = cursor.fetchone()

    if entry is None:
        raise HTTPException(
            status_code=404,
            detail="Weight entry not found"
        )

    # Delete the weight entry
    cursor.execute(
        "DELETE FROM weight_entries WHERE id = %s",
        (entry_id,)
    )

    connection.commit()

    return {       #type: ignore
        "message": "Weight entry deleted successfully",
        "id": entry_id
    }

@app.post("/notes")
def create_note(note: Note):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (note.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Make sure the note is not empty
    if not note.content.strip():
        raise HTTPException(
            status_code=400,
            detail="Note content cannot be empty"
        )

    # Save the note
    cursor.execute(
        """
        INSERT INTO notes
        (user_id, content, date)
        VALUES (%s, %s, %s)
        """,
        (
            note.user_id,
            note.content,
            note.date
        )
    )

    connection.commit()

    note_id = cursor.lastrowid

    return {      #type: ignore
        "id": note_id,
        "user_id": note.user_id,
        "content": note.content,
        "date": note.date
    }

@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get the user's notes
    cursor.execute(
        """
        SELECT
            id,
            user_id,
            content,
            date
        FROM notes
        WHERE user_id = %s
        ORDER BY date DESC, id DESC
        """,
        (user_id,)
    )

    notes = cursor.fetchall()

    return [    #type: ignore
        {
            "id": note[0],
            "user_id": note[1],
            "content": note[2],
            "date": str(note[3])
        }
        for note in notes
    ]
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the note exists
    cursor.execute(
        "SELECT * FROM notes WHERE id = %s",
        (note_id,)
    )

    existing_note = cursor.fetchone()

    if existing_note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    # Check that the user exists
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (note.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Make sure the note is not empty
    if not note.content.strip():
        raise HTTPException(
            status_code=400,
            detail="Note content cannot be empty"
        )

    # Update the note
    cursor.execute(
        """
        UPDATE notes
        SET user_id = %s,
            content = %s,
            date = %s
        WHERE id = %s
        """,
        (
            note.user_id,
            note.content,
            note.date,
            note_id
        )
    )

    connection.commit()

    return {      #type: ignore
        "message": "Note updated successfully",
        "id": note_id,
        "user_id": note.user_id,
        "content": note.content,
        "date": note.date
    }

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    # Check that the note exists
    cursor.execute(
        "SELECT * FROM notes WHERE id = %s",
        (note_id,)
    )

    note = cursor.fetchone()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    # Delete the note
    cursor.execute(
        "DELETE FROM notes WHERE id = %s",
        (note_id,)
    )

    connection.commit()

    return {    #type: ignore
        "message": "Note deleted successfully",
        "id": note_id
    }

@app.get("/users/{user_id}/dashboard")
def get_dashboard(user_id: int):
    # Check that the user exists
    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=404, detail="User not found")

    # Get today's calorie and protein summary
    cursor.execute(
        """
        SELECT
            COALESCE(SUM(foods.calories * food_entries.quantity), 0) AS calories_consumed,
            COALESCE(SUM(foods.protein * food_entries.quantity), 0) AS protein_consumed
        FROM food_entries
        JOIN foods ON food_entries.food_id = foods.id
        WHERE food_entries.user_id = %s
        AND food_entries.entry_date = CURDATE()
        """,
        (user_id,)
    )

    summary = cursor.fetchone()

    # Calculate calorie target
    if user["sex"].lower() == "male":
        bmr = (
            (10 * float(user["weight"]))
            + (6.25 * float(user["height"]))
            - (5 * user["age"])
            + 5
        )
    else:
        bmr = (
            (10 * float(user["weight"]))
            + (6.25 * float(user["height"]))
            - (5 * user["age"])
            - 161
        )

    activity_factor = ACTIVITY_FACTORS.get(
        user["activity_level"].lower()
    )

    if activity_factor is None:
        cursor.close()
        raise HTTPException(
            status_code=400,
            detail="Invalid activity level"
        )

    tdee = bmr * activity_factor

    if user["goal"].lower() == "weight loss":
        daily_calorie_target = tdee - 500
    elif user["goal"].lower() == "weight gain":
        daily_calorie_target = tdee + 300
    else:
        daily_calorie_target = tdee

    calories_consumed = int(summary["calories_consumed"])
    protein_consumed = float(summary["protein_consumed"])
    calories_remaining = round(daily_calorie_target) - calories_consumed

    # Get starting weight
    cursor.execute(
        """
        SELECT weight
        FROM weight_entries
        WHERE user_id = %s
        ORDER BY date ASC, id ASC
        LIMIT 1
        """,
        (user_id,)
    )

    starting_weight = cursor.fetchone()

    # Get current weight
    cursor.execute(
        """
        SELECT weight
        FROM weight_entries
        WHERE user_id = %s
        ORDER BY date DESC, id DESC
        LIMIT 1
        """,
        (user_id,)
    )

    current_weight = cursor.fetchone()

    cursor.close()
    connection.close()

    if starting_weight and current_weight:
        starting = float(starting_weight["weight"])
        current = float(current_weight["weight"])
        weight_change = current - starting
    else:
        starting = None
        current = None
        weight_change = None

    return {     #type: ignore
        "user_id": user_id,
        "calories": {
            "target": round(daily_calorie_target),
            "consumed": calories_consumed,
            "remaining": calories_remaining
        },
        "protein": {
            "consumed": protein_consumed
        },
        "weight": {
            "starting": starting,
            "current": current,
            "change": weight_change
        }
    }

from pydantic import BaseModel

class WeightEntry(BaseModel):
    user_id: int
    weight: float
    entry_date: str

@app.post("/weight-entries")
def add_weight(entry: WeightEntry):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weight_entries (user_id, weight, entry_date) VALUES (%s, %s, %s)",
        (entry.user_id, entry.weight, entry.entry_date)
    )
    conn.commit()
    conn.close()
    return {"message": "Weight entry added successfully"}

@app.get("/users/{user_id}/weight-history")
def get_weight_history(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT entry_date, weight FROM weight_entries WHERE user_id = %s ORDER BY entry_date ASC",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [{"entry_date": r[0], "weight": r[1]} for r in rows]
