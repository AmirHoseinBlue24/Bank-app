class Balance:
    def __init__(self, user):
        self.user = user

    def show(self):
        print("================= Balance ==================")
        print(self.user.get('balance'))