const userId = 1;

async function loadFoods() {
    try {
        const response = await fetch(
            "http://127.0.0.1:8001/foods"
        );

        if (!response.ok) {
            throw new Error("Failed to load foods");
        }

        const foods = await response.json();

        const foodSelect = document.getElementById("food-id");

        foods.forEach(function (food) {
            const option = document.createElement("option");

            option.value = food.id;
            option.textContent = food.name;

            foodSelect.appendChild(option);
        });

    } catch (error) {
        console.error("Error loading foods:", error);
    }
} 

async function loadDashboard() {
    try {
        const response = await fetch(
            `http://127.0.0.1:8001/users/${userId}/dashboard`
        );

        if (!response.ok) {
            throw new Error("Failed to load dashboard");
        }

        const data = await response.json();

        document.getElementById("calorie-target").textContent =
            data.calories.target;

        document.getElementById("calories-consumed").textContent =
            data.calories.consumed;

        document.getElementById("calories-remaining").textContent =
            data.calories.remaining;

        document.getElementById("protein-consumed").textContent =
            data.protein.consumed;

        document.getElementById("starting-weight").textContent =
            data.weight.starting;

        document.getElementById("current-weight").textContent =
            data.weight.current;

        document.getElementById("weight-change").textContent =
            data.weight.change;

    } catch (error) {
        console.error("Error loading dashboard:", error);
    }
}

document.getElementById("food-entry-form").addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

        const foodId = Number(
            document.getElementById("food-id").value
        );

        const quantity = Number(
            document.getElementById("quantity").value
        );

        const meal = document.getElementById("meal").value;

        try {
            const response = await fetch(
                "http://127.0.0.1:8001/food-entries",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        user_id: userId,
                        food_id: foodId,
                        quantity: quantity,
                        meal: meal
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.detail || "Failed to add food"
                );
            }

            console.log("Food added:", data);

            document.getElementById("food-entry-form").reset();

            await loadDashboard();

        } catch (error) {
            console.error("Error adding food:", error);
            alert(error.message);
        }
    }
);

loadFoods();
loadDashboard();