from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hasher:
    @staticmethod
    def get_hash_password(password):
        return password_context.hash(password)
    @staticmethod
    def verify_password(password, hashed_password):
        return password_context.verify(password, hashed_password)