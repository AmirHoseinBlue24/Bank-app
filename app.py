from database import Database
from auth import Auth
from balance import Balance
from trans_action import Transaction



class App:
    def __init__(self):
        self.database = Database()
        self.auth = Auth(self.database)
        self.current_user = None

    def run(self):
        self.current_user = self.auth.login()
        if self.current_user is None:
            return
        self.main_menu()

    def main_menu(self):
        while True:
            print("================  Main  ================")
            print("Lotfan Khedmat Mored Nazar Ra Entekhab Konid")
            print("1. Mohoodi Hesab")
            print("2. Darkhast Vam")
            print("3. Enteghal")
            print("4. Khorooj")
            choice = input("Lotfan Gozine Mored Nazar Ra Vared Konid: ")

            if choice == "1":
                Balance(self.current_user).show()
            elif choice == "2":
                print("Darkhast Shoma Ersal Gardid!")
            elif choice == "3":
                Transaction(self.database).transfer(self.current_user)
            elif choice == "4":
                self.database.save()
                print("Khorooj Az Barname")
                break
            else:
                print("Gozine Eshtebah Ast! Dobare Talash Konid")

app = App()
app.run()