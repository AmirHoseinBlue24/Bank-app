import json

class Database:
    def __init__(self):
        self.main_data = []
        self.users = []
        self.pay_data = []
        self.load()

    def load(self):
        with open("database.json", "r", encoding="utf-8") as f:
            self.main_data = json.load(f)
        with open("users.json", "r", encoding="utf-8") as f:
            self.users = json.load(f)
        try:
            with open("pay_database.json", "r", encoding="utf-8") as f:
                self.pay_data = json.load(f)
        except FileNotFoundError:
            self.pay_data = []

    def save(self):
        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(self.main_data, f, indent=4)
        with open("users.json", "w", encoding="utf-8") as f:
            json.dump(self.users, f, indent=4)
        with open("pay_database.json", "w", encoding='utf-8') as f:
            json.dump(self.pay_data, f, indent=4, ensure_ascii=False)

    def get_main(self):
        return self.main_data

    def get_users(self):
        return self.users

    def get_pay(self):
        return self.pay_data

    def set_users(self, users):
        self.users = users

    def set_main(self, main_data):
        self.main_data = main_data
    def set_pay(self, pay_data):
        self.pay_data = pay_data