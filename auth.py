from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM
# 
def verify_token(token : str):
    try:
        token = token.strip()
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get('sub')
# 
    except JWTError as e:
        return {"Error": "Verification failed.", "message": e}
    # 
#print(verify_token(b"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJoaW1tdSIsImlhdCI6MTc0NTk0NTk2OCwiZXhwIjoxNzQ1OTQ5NTY4fQ.93F0RUJspHARxxZOnD9OEerfgKy74rKUziHScfb6Ah8"))

def get_current_user(token):
    try:
        user = verify_token(token=token)
        return user
    except Exception as e:
        print(str(e))
        return None