from fastapi import APIRouter, Depends, HTTPException, status
from database import get_database
from sqlalchemy.orm import Session
from models.user import UserModel, UserUpdate, UserResponseModel
from models.login import *
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from utils.login_utils import get_password_hash, verify_password, SECRET_KEY, ALGORITHM, OAUTH2SCHEME, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm
from tables.user_base import UserBase

router = APIRouter()

def create_response_model(user: UserBase) -> UserResponseModel:
        return UserResponseModel(email=user.email,
                                name=user.name,
                                balance=user.balance,
        )

@router.post("/users")
async def create_user(user: UserModel, 
                      db: Session = Depends(get_database)):
    try:
        hashed_password = get_password_hash(user.password)
        new_user = UserModel(email=user.email,
                            name=user.name,
                            balance=user.balance,
                            password=hashed_password)
        return UserService(db).create_user(new_user)
    except UserAlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except UserWithoutName as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/users")
async def get_users(db: Session = Depends(get_database)):
    return UserService(db).get_users() 

@router.get("/users/{user_email}")
async def get_user(user_email: str,
                   db: Session = Depends(get_database)):
    try:
        return create_response_model(UserService(db).get_user(user_email))
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        

@router.put("/users/{user_email}")
async def update_user(user_email: str,
                      user_update: UserUpdate,
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).update_user(user_email, user_update)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.delete("/users/{user_email}")
async def delete_user(user_email: str, 
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).delete_user(user_email)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    

# Login

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return  jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(user):
    registered_user = get_user(user.email)
    if registered_user and verify_password(user.password, registered_user.password):
        return registered_user
        
@router.put("/login")
async def login(user: UserLoginModel,
                 db: Session = Depends(get_database)):
    try:
        registered_user = UserService(db).get_user(user.email)
        if not verify_password(user.password, registered_user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        
    
async def get_current_user(token: str = Depends(OAUTH2SCHEME)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers="")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if not email:
            raise exception
        token_data = TokenData(email=email)
    except JWTError:
        raise exception
    
    user = get_user(user_email=token_data.email)
    if not user:
        raise exception
    
    return user

async def get_current_active_user(current_user = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    
    return current_user

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email o contraseña incorrecta")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub", user.email}, 
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}