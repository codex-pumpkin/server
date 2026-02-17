
import bcrypt

def hash_password(password: str) -> str:
    """Hash password."""
    salt:bytes = bcrypt.gensalt()
    hashed:bytes = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode(encoding="utf-8")

def validate_password(hashed: str, password: str) -> bool:
    """Validate password."""
    return bcrypt.checkpw(password.encode(), hashed.encode())

def _main() -> None:
    """Main."""
    hashed = hash_password("asd")
    print(hashed)
    print(validate_password(hashed, "asd"))

if __name__ == "__main__":
    _main()