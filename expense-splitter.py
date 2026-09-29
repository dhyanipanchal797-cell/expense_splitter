"""
Expense Splitter (Splitwise-style)
-----------------------------------
This is a small project I made to solve a problem I've actually faced — 
splitting expenses with roommates or friends and figuring out who owes what, 
without everyone paying each other back and forth separately.
 
Author: Dhyani Panchal
"""
 
 
class ExpenseSplitter:
    def __init__(self):
        # net balance of each person .
        # +ve means they should receive money.
        # -ve means they need to pay .
        self.balances = {}
 
    def add_person(self, name):
        if name not in self.balances:
            self.balances[name] = 0.0
            print("Added " + str(name) + " to the group.")
        else:
            print(str(name) + " is already in the group.")
 
    def add_expense(self, payer, amount, participants):
        # add a new expense
        
        if payer not in self.balances:
            print(str(payer) + " is not part of the group.")
            return
 
        for person in participants:
            if person not in self.balances:
                print(str(person) + " is not part of the group.")
                return
 
        share = amount / len(participants)
 
        # The payer paid full amount , so add it to their balance
        self.balances[payer] += amount
 
        # Everyone (including payer) pays their share
        for person in participants:
            self.balances[person] -= share
 
        print("Recorded: " + str(payer) + "  paid " + format(amount, " .2f") +
               " , split equally among " + str(participants) +  
              "(" + format(share , " .2f" ) + " each).")
 
    def show_balances(self):
        #Show current balances of everyone
        print()
        print("--- Current Balances ---")
        for person, balance in self.balances.items():
            if balance > 0:
                print(str(person) + " is owed " + format(balance , ".2f"))
            elif balance < 0:
                print(str(person) + " owes " +  format(abs(balance) , ".2f"))
            else:
                print(str(person) + " is settled up.")
        print()
        print("-------------------------")
 
    def settle_up(self):
       # find who should receive money and who should pay
        creditors = [(name, bal) for name, bal in self.balances.items() if bal > 0.01]
        debtors = [(name, bal) for name, bal in self.balances.items() if bal < -0.01]

        
        creditors.sort(key=lambda x: x[1], reverse=True)
        debtors.sort(key=lambda x: x[1])
 
        transactions = []
        i, j = 0, 0
 
        # match people who owe with people who should receive
        while i < len(debtors) and j < len(creditors):
            debtor_name, debt_amount = debtors[i]
            creditor_name, credit_amount = creditors[j]
 
            payment = min(-debt_amount, credit_amount)
            transactions.append((debtor_name, creditor_name, payment))
 
            debtors[i] = (debtor_name, debt_amount + payment)
            creditors[j] = (creditor_name, credit_amount - payment)
 
            if abs(debtors[i][1]) < 0.01:
                i += 1
            if creditors[j][1] < 0.01:
                j += 1
 
        print("--- Settlement Plan ---")
        if not transactions:
            print("Everyone is already settled up!")
        for debtor, creditor, amount in transactions:
            print(str(debtor) + " should pay " + str(creditor) + " : "  + format(amount , " .2f" ))
        print()
        print("-----------------------")
 
 
def run_interactive_mode(splitter):
    # lets user add people and expenses themselves
    print()
    print("=== Interactive Mode ===")
    print("Type 'done' at any prompt to stop adding people.")
    print()
 
    while True:
        name = input("Enter a name to add (or type 'done'): ").strip()
        if name.lower() == "done":
            break
        if name:
            splitter.add_person(name)

    print() 
    print("Now add expenses. Type 'done' as payer name to stop.")
    print()
 
    while True:
        payer = input("Who paid? (or 'done'): ").strip()
        if payer.lower() == "done":
            break
 
        try:
            amount = float(input("How much? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
 
        participants_raw = input("Who shared this expense? (comma-separated names): ")
        participants = [p.strip() for p in participants_raw.split(",") if p.strip()]
 
        if not participants:
            print("Please enter at least one name . ")
            continue
 
        splitter.add_expense(payer, amount, participants)
 
    splitter.show_balances()
    splitter.settle_up()
 
 
def main():
    splitter = ExpenseSplitter()
 
    print("=== Expense Splitter ===")
    print("1. Run demo (sample trip data)")
    print("2. Enter your own people and expenses")
    choice = input("Choose an option 1 or 2: ").strip()
 
    if choice == "2":
        run_interactive_mode(splitter)
        return
 
    # demo data
    print()
    print("Running demo...")
    print()
 
    for name in ["Dhyani", "Himanshi", "Janhvi"]:
        splitter.add_person(name)
 
    print()
    splitter.add_expense("Dhyani", 900, ["Dhyani", "Himanshi", "Janhvi"])
    splitter.add_expense("Himanshi", 300, ["Himanshi", "Janhvi"])
    splitter.add_expense("Janhvi", 600, ["Dhyani", "Janhvi"])
 
    splitter.show_balances()
    splitter.settle_up()
 
 
if __name__ == "__main__":
    main()
 
