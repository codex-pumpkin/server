
import bcrypt

def hash_password(password: str) -> str:
    salt:bytes = bcrypt.gensalt()
    hashed:bytes = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode(encoding="utf-8")

def validate_password(hashed: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def _main() -> None:
    hashed = hash_password("asd")
    print(hashed)
    print(validate_password(hashed, "asd"))

if __name__ == "__main__":
    _main()