

class WebApp:
    def __init__(self):
        self.database = Database(self.database)
    
    def auth(self):
        st.header("Login")
        users = self.database.get_users()
        c = 0
        while c < 3:
            username = st.text_input("Username: ")
            user_found = None
            for user in users:
                if username == user.get('user'):
                    user_found = username

