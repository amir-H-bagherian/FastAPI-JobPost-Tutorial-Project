from sqlalchemy.orm import Session

from models.users import User
from core.hashing import Hasher


def create_new_user(user, db: Session):
    new_user = User(
        username=user.username,
        email = user.email,
        hashed_password=Hasher.get_hash_password(user.password),
        is_active=True,
        is_superuser=False
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user