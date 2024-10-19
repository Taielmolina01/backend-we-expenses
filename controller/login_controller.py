from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from models.login import UserLoginModel, TokenData
from sqlalchemy.orm import Session
from database import get_database
from service.user_service import UserService
from service.exceptions.users_exceptions import UserNotRegistered
from datetime import datetime, timedelta
from jose import JWTError, jwt
from controller.user_controller import get_user
from models.login import Token, TokenData

router = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_Scheme = OAuth2PasswordBearer(tokenurl="token")

SECRET_KEY = "3088d5c87b937d63a615e7691368919c6b714d0481826052c24f86ee73ef157549"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    password_context.hash(plain_password)

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
    
async def get_current_user(token: str = Depends(oauth_2_Scheme)):
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