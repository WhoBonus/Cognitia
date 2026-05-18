from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI app
app = FastAPI(title="Beginner Users API")

# 2. Define the data we expect from the user using Pydantic.
# This ensures that whenever someone creates a user, they MUST provide a name and email.
class UserCreate(BaseModel):
    name: str
    email: str

# 3. Our "Fake Database"
# This is just a Python list. It lives in the computer's memory (RAM).
fake_users_db = []
current_id = 1  # We will use this to assign a unique ID to each new user

# --- ROUTES (API ENDPOINTS) ---

# GET / -> Returns a simple greeting
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

# GET /users -> Lists all users in our fake database
@app.get("/users")
def get_users():
    return fake_users_db

# POST /users -> Creates a new user
@app.post("/users")
def create_user(user: UserCreate):
    global current_id
    
    # Create a dictionary representing the new user, adding the auto-incremented ID
    new_user = {
        "id": current_id,
        "name": user.name,
        "email": user.email
    }
    
    # Save the new user to our fake database list
    fake_users_db.append(new_user)
    
    # Increase the ID by 1 so the next user gets a different ID
    current_id += 1
    
    # Return the newly created user data back to the client
    return new_user