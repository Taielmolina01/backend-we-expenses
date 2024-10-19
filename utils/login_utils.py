from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2SCHEME = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "3088d5c87b937d63a615e7691368919c6b714d0481826052c24f86ee73ef157549"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return PASSWORD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return PASSWORD_CONTEXT.hash(plain_password)

