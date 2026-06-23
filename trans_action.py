from random import randint
import jdatetime

banks = {
        '603799': 'بانک ملی',
        '603770': 'بانک صادرات',
        '603769': 'بانک کشاورزی',
        '589210': 'بانک سپه',
        '610433': 'بانک ملت',
        '628023': 'بانک مسکن',
        '627648': 'بانک توسعه صادرات',
        '627961': 'بانک صنعت و معدن',
        '627353': 'بانک تجارت',
        '589463': 'بانک رفاه',
        '639347': 'بانک پاسارگاد',
        '627412': 'بانک اقتصاد نوین',
        '622106': 'بانک پارسیان',
        '627488': 'بانک کارآفرین',
        '621986': 'بانک سامان',
        '639346': 'بانک سینا',
        '639607': 'بانک سرمایه',
        '502806': 'بانک شهر',
        '502938': 'بانک دی',
        '627381': 'بانک انصار',
        '639599': 'بانک قوامین',
    }

class Transaction:
    def __init__(self, database):
        self.database = database
        self.banks = banks

    def transfer(self, current_user):
        print("================= Enteghal ==================")
        
        card_number = input("Shomare Kart Fard: ")
        if len(card_number) != 16:
            print("Shomare Kart Bayad 16 Ragham Bashad!")
            return

        prefix = card_number[:6]
        if prefix not in self.banks:
            print("Shomare Kart Moetabar Nist!")
            return

        users = self.database.get_users()
        main_data = self.database.get_main()
        
        target_user = None
        if prefix == "603770":
            for user in users:
                if user.get('card') == card_number:
                    target_user = user
                    break
        else:
            for user in main_data:
                if user.get('card') == card_number:
                    target_user = user
                    break

        if target_user is None:
            print("Shomare Kart Dar Database Yaft Nashod!")
            return

        if target_user.get('is_active') == False:
            print("Hesab maghsad Mored Nazar Gheyr Faal Ast!")
            return

        print(f"Shomare Kart Motabar Ast ({self.banks[prefix]} - {target_user.get('name')})")

        try:
            amount = int(input("Meghdar Mored Nazar Ra Vared Konid: "))
        except ValueError:
            print("Meghdar Eshtebah Ast!")
            return

        if amount > current_user.get('balance'):
            print("Mojoodi Kafi Nist!")
            return

        if amount < 10000000:
            if prefix == "603770":
                fee = 45
            else:
                fee = 900

            if current_user.get('balance') < amount + fee:
                print("Mojoodi Baraye Pardakht KarMozd Kafi Nist!")
                return

            current_user['balance'] -= (amount + fee)
            target_user['balance'] += amount

            code = randint(10000, 99999)
            pay_data = self.database.get_pay()
            for p in pay_data:
                if p.get('code') == code:
                    code = randint(10000, 99999)

            pay_data.append({
                'at_bank': 'بانک صادرات',
                'to_bank': self.banks[prefix],
                'to_card': card_number,
                'at_card': current_user.get('card'),
                'code': code,
                'date': str(jdatetime.datetime.now())
            })
            self.database.set_pay(pay_data)

        else:
            print("Baraye Mabalegh Bishtar Az 10,000,000 Rials Enteghal Vajh Paya Estefade Konid")
            print("1. Shomare Hesab")
            print("2. Shomare Sheba")
            choice = input("Yeki Ra Entekhab Konid: ")

            if choice == "1":
                account_no = input("Shomare Hesab Maghsad: ")
                target = None
                for user in main_data:
                    if user.get('hesab') == account_no:
                        target = user
                        break
                if target is None:
                    for user in users:
                        if user.get('account_no') == account_no:
                            target = user
                            break
                if target is None:
                    print("Shomare Hesab Yaft Nashod!")
                    return
                if target.get('is_active') == False:
                    print('Hesab Maghsad Gheyr Faal Ast!')
                    return
                if current_user.get('balance') < amount + 25:
                    print("Mojoodi Baraye KarMozd Kafi Nist!")
                    return
                current_user['balance'] -= (amount + 25)
                target['balance'] += amount
                print("Enteghal Az Tarigh Hesab Anjam Shod!")

            elif choice == "2":
                sheba_no = input("Shomare Sheba Maghsad: ")
                target = None
                for user in main_data:
                    if user.get('sheba') == sheba_no:
                        target = user
                        break
                if target is None:
                    for user in users:
                        if user.get('sheba_no') == sheba_no:
                            target = user
                            break
                if target is None:
                    print("Shomare Sheba Yaft Nashod!")
                    return
                if target.get('is_active') == False:
                    print('Hesab Maghsad Gheyr Faal Ast!')
                    return
                if current_user.get('balance') < amount + 900:
                    print("Mojoodi Baraye KarMozd Kafi Nist!")
                    return
                current_user['balance'] -= (amount + 900)
                target['balance'] += amount
                print("Enteghal Az Tarigh Sheba Anjam Shod!")

            else:
                print("Gozine Eshtebah Ast!")
                return

        for i in range(len(users)):
            if users[i].get('card') == current_user.get('card'):
                users[i] = current_user
            if users[i].get('card') == target_user.get('card'):
                users[i] = target_user

        for i in range(len(main_data)):
            if main_data[i].get('card') == current_user.get('card'):
                main_data[i] = current_user
            if main_data[i].get('card') == target_user.get('card'):
                main_data[i] = target_user

        self.database.set_users(users)
        self.database.set_main(main_data)
        self.database.save()
        print("Enteghal Anjam Shod!")