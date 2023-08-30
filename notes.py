denominations = [500, 200, 50]

while True:
    amount = int(input("Enter the amount to withdraw: "))
    
    if amount <= 0 or amount % 50 != 0:
        print("Invalid amount entered. Please enter a valid amount (multiple of 50).")
    else:
        notes_count = {}
        for denomination in denominations:
            print("denominations::::::",denomination)  #500
            if amount >= denomination:
                #print("given amount:::::::",amount)  #1000
                count = amount // denomination 
                #print("count::::::",count)   #2
                notes_count[denomination] = count  #500(key)=2(count)
                #print("notes_count:::::",notes_count)
                amount -= count * denomination   #for example count is 1 and denomination is 500 then 500 - original amount the it will give u certain amount
                #print("amount:::::::",amount)

        print("Dispensing the following notes:")
        for denomination, count in notes_count.items():
            #print("denominations11111",denominations)
            #print("count111111111111111",count)
            print(f"{denomination} notes: {count}")

    choice = input("Do you want to continue (C) or cancel (X)? ").upper()
    if choice != 'C':
        print("Transaction cancelled.")
        break




















# class ATM:
#     def __init__(self):
#         self.denominations = [500, 200, 50]

#     def validate_amount(self, amount):
#         if amount <= 0 or amount % 50 != 0:
#             return False
#         return True

#     def calculate_notes(self, amount):
#         notes_count = {}
#         for denomination in self.denominations:
#             if amount >= denomination:
#                 count = amount // denomination
#                 notes_count[denomination] = count
#                 amount -= count * denomination
#         return notes_count

#     def dispense_cash(self, amount):
#         if not self.validate_amount(amount):
#             print("Invalid amount entered. Please enter a valid amount (multiple of 50).")
#             return
        
#         notes_count = self.calculate_notes(amount)

#         print("Dispensing the following notes:")
#         for denomination, count in notes_count.items():
#             print(f"{denomination} notes: {count}")

# def main():
#     atm = ATM()
    
#     while True:
#         amount = int(input("Enter the amount to withdraw: "))
        
#         atm.dispense_cash(amount)
        
#         choice = input("Do you want to continue (C) or cancel (X)? ").upper()
#         if choice != 'C':
#             print("Transaction cancelled.")
#             break

# if __name__ == "__main__":
#     main()
