from fastapi import FastAPI
from controller.group_controller import router as group_controller
from controller.user_controller import router as user_controller
from controller.payment_controller import router as payment_controller
from controller.debt_controller import router as debt_controller
from controller.user_invitation_controller import router as user_invitation_controller
from controller.users_by_groups_controller import router as users_by_groups_controller
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.head("/")
def head():
    return

@app.get("/")
def home():
    return {"message": "Bienvenido a OurExpenses"}

app.include_router(debt_controller)
app.include_router(group_controller)
app.include_router(payment_controller)
app.include_router(user_controller)
app.include_router(user_invitation_controller)
app.include_router(users_by_groups_controller)

app.title = "OurExpenses"
app.version = "1.0"

origins = [
    "http://localhost:5173",
    "https://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)