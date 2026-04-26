from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

SECRET = "secret123"
pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd_context.hash(password)

def create_token(username):
    payload = {"user": username, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET, algorithm="HS256")
