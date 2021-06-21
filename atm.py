class Atm :
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkbalance(self):
        print("your balance is 20,000")
    def withdrawal(self,amount):
        new_amount=20000-amount
        print("your remaining balancy is"+str(new_amount))
def main ():
    card_number=input("enter your card number")
    pin_number=input("enter your pin number")
    new_user=Atm(card_number,pin_number)
    print("choose your activity 1.balnce enquiry,2.withdrawal")
    activity=int(input("enter the activity number"))
    if(activity==1):
        new_user.checkbalance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        new_user.withdrawal(amount)
    else:
        print("enter valid number")
if __name__==" __main__":
    main()