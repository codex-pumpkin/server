import jwt
import datetime
from src.core.settings import settings
from typing import Optional, Dict

def encode_jwt(
    payload:dict,
    secret_key: str = settings.jwt_settings.secret_key,
    algorithm: str = settings.jwt_settings.algorithm,
    expire_minutes: int = settings.jwt_settings.expire_time,
    time_delta: Optional[datetime.timedelta] = None
) -> str:
    """Encode jwt."""
    payload_copy = payload.copy()
    now = datetime.datetime.now(datetime.UTC)
    if time_delta is not None:
        expire = now + time_delta
    else:
        expire = now + datetime.timedelta(minutes=expire_minutes)
    payload_copy.update(
        toc=now.timestamp(),
        exp=expire.timestamp()
    )
    return jwt.encode(
        payload_copy,
        secret_key,
        algorithm=algorithm
    )

def decode_jwt(
    encoded:str,
    secret_key:str = settings.jwt_settings.secret_key,
    algorithm:str = settings.jwt_settings.algorithm
   ) -> Dict:
    """Decode jwt."""
    return jwt.decode(
        encoded,
        secret_key,
        algorithms=algorithm
    )

def check_if_jwt_valid(jwt_token:str) -> bool:
    """Check if jwt valid."""
    try:
        data:Dict = decode_jwt(jwt_token)
    except Exception as e:
        return False
    return True


def _main():
    """Main."""
    encoded = encode_jwt({"id":"ast"})
    print(encoded)
    decoded = decode_jwt(encoded)
    print(decoded)
    print(check_if_jwt_valid(encoded))

if __name__ == "__main__":
    _main()