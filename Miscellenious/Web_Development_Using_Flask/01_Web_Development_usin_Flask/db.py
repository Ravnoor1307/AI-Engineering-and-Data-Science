import json
from pathlib import Path

from werkzeug.security import check_password_hash, generate_password_hash

class Database:
    def __init__(self, db_file):
        self.db_file = Path(db_file)
        self.data = self.load_data()

    def load_data(self):
        try:
            with self.db_file.open('r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        if not isinstance(data, dict):
            raise ValueError(f'User database must contain a JSON object: {self.db_file}')
        return data

    def save_data(self):
        with self.db_file.open('w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def add_user(self, username, password, fullname=''):
        if username in self.data:
            return False
        self.data[username] = {
            'fullname': fullname,
            'password': generate_password_hash(password),
        }
        self.save_data()
        return True

    def validate_user(self, username, password):
        user = self.search_user(username)
        if not user or not isinstance(user.get('password'), str):
            return False

        stored_password = user['password']
        if stored_password.startswith(('pbkdf2:', 'scrypt:')):
            return check_password_hash(stored_password, password)

        # Upgrade passwords saved in plaintext by the previous database format.
        if stored_password == password:
            user['password'] = generate_password_hash(password)
            self.save_data()
            return True
        return False

    def search_user(self, username):
        if not isinstance(username, str):
            return None
        return self.data.get(username.strip().lower())