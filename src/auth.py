import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import sha256
from typing import Optional

@dataclass
class User:
    username: str
    password_hash: str
    password_reset_token: Optional[str] = None
    password_reset_expires: Optional[datetime] = None

class Auth:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str):
        password_hash = sha256(password.encode()).hexdigest()
        self.users[username] = User(username, password_hash)

    def request_password_reset(self, username: str):
        user = self.users.get(username)
        if user:
            token = sha256(f"{username}{datetime.now().isoformat()}".encode()).hexdigest()
            user.password_reset_token = token
            user.password_reset_expires = datetime.now() + timedelta(hours=1)
            return token
        return None

    def reset_password(self, username: str, token: str, new_password: str):
        user = self.users.get(username)
        if user and user.password_reset_token == token and user.password_reset_expires > datetime.now():
            user.password_hash = sha256(new_password.encode()).hexdigest()
            user.password_reset_token = None
            user.password_reset_expires = None
            return True
        return False

    def send_password_reset_email(self, username: str, token: str):
        # Simulate sending an email
        print(f"Password reset email sent to {username} with token {token}")

    def authenticate(self, username: str, password: str):
        user = self.users.get(username)
        if user and user.password_hash == sha256(password.encode()).hexdigest():
            return True
        return False
