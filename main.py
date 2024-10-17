from fastapi import FastAPI
from controller.group_controller import router as group_controller
from controller.user_controller import router as user_controller
from controller.payment_controller import router as payment_controller
from controller.debt_controller import router as debt_controller
from controller.user_invitation_controller import router as user_invitation_controller
from controller.users_by_groups_controller import router as users_by_groups_controller
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.head("/")
def head():
    return

@app.get("/")
def home():
    return {"message": "Bienvenido a WeExpenses"}

app.include_router(group_controller)
app.include_router(user_controller)
app.include_router(payment_controller)
app.include_router(debt_controller)
app.include_router(user_invitation_controller)
app.include_router(users_by_groups_controller)

app.title = "OurExpenses"
app.version = "1.0"
