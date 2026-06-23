class Auth:
    def __init__(self, users):
        self.users = users
        self.current_user = None

    def login(self):
        print("============  Login  =============")
        users = self.users.get_users()
        c = 0
        while c < 3:
            username = input("Lotfan Username Ra Vared Konid: ")
            user_found = None
            for user in users:
                if username == user.get('user'):
                    user_found = user
                    break

            if user_found is None:
                c += 1
                print(f"Username Peyda Nashod! Talash {c} az 3")
                if c == 3:
                    print("3 Bar Username Eshtebah Vared Shod! Bye")
                    return None
                continue

            if user_found.get('is_active') == False:
                print("Hesab Shoma Gheyr Faal Ast! Lotfan Be Bank Moraje Konid")
                return None

            count = 0
            while count < 3:
                password = input("Lotfan Ramz Vorood Ra Vared Konid: ")
                if password == user_found.get('pass'):
                    print(f"Khosh Amadid {user_found.get('name')}")
                    self.current_user = user_found
                    return user_found
                else:
                    count += 1
                    print(f"Ramz Eshtbah Ast! Talash {count} az 3")

            print("3 Bar Pass Eshtebah Vared Shod! Bye")
            return None