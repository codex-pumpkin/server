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
    """
    Encode payload into a signed JWT with issue and expiry timestamps.

    @param payload (dict): Claims dictionary to be embedded into the JWT body.
    @param secret_key (str, optional): Signing key used for JWT encoding.
    @param algorithm (str, optional): JWT signing algorithm identifier.
    @param expire_minutes (int, optional): Expiration interval in minutes when
    @param `time_delta` is not provided.
    @param time_delta (Optional[datetime.timedelta], optional): Explicit expiry delta
    @param override for token lifetime control.

    @return str: Encoded JWT string suitable for authorization headers.
    """
    payload_copy = payload.copy()
    now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)
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
    """
    Decode and validate a JWT using configured secret and algorithm.

    @param encoded (str): Encoded JWT token string.
    @param secret_key (str, optional): Verification key used for decoding.
    @param algorithm (str, optional): Accepted signing algorithm.

    @return Dict: Decoded JWT claims payload.
    """
    return jwt.decode(
        encoded,
        secret_key,
        algorithms=algorithm
    )

def check_if_jwt_valid(jwt_token:str) -> bool:
    """
    Check whether a JWT can be decoded successfully.

    @param jwt_token (str): Token string to validate.

    @return bool: `True` if token decoding succeeds, otherwise `False`.
    """
    try:
        data:Dict = decode_jwt(jwt_token)
    except Exception as e:
        return False
    return True


def _main():
    """
    Run a small local sanity check for encode/decode helpers.

    @return None: Prints encoded token, decoded payload, and validity status.
    """
    encoded = encode_jwt({"id":"ast"})
    print(encoded)
    decoded = decode_jwt(encoded)
    print(decoded)
    print(check_if_jwt_valid(encoded))

if __name__ == "__main__":
    _main()
