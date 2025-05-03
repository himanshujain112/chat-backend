from jose import jwt
from config import SECRET_KEY, ALGORITHM

def generate_token(user_id):
    return jwt.encode({"sub": user_id}, SECRET_KEY, algorithm=ALGORITHM)

print(generate_token("user_1"))
print(generate_token("user_2"))
