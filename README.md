# Expense Splitter
A command-line tool written in Python designed to split group expenses—similar to Splitwise. It calculates individual balances and generates an optimized settlement plan to minimize the number of cash transfers required between roommates or friends.

Features :

Dynamic Group Management: Add any number of participants to the expense group.
Flexible Expense Splitting: Record who paid and split the amount equally among any subset of participants.
Real-time Balance Tracking: View who is owed money, who owes money, and who is fully settled up.
Optimized Settlement Algorithm: Automatically matches debtors with creditors to compute the minimum number of transactions needed to clear all debts.
Dual Modes: Choose between a pre-loaded sample trip demo or an interactive mode to input your own custom names and expenses.

Project Structure :

expense-splitter/
│
├── expense-splitter.py   # Core application script
└── README.md             # Project documentation

Getting Started :

    Prerequisites :
    Python 3.x installed on your system.

    Running the Script :
    Clone or download the script file (expense-splitter.py).
    Open your terminal or command prompt in the directory containing the file.
    Run the script using Python: python expense-splitter.py
    Choose between the Demo Mode (to see a pre-configured sample group) or Interactive Mode (to input your own custom names and expenses).

Code Overview :

    The script is structured around a core ExpenseSplitter class:
    add_person(name): Registers a new user into the tracking ledger.
    add_expense(payer, amount, participants): Deducts shares, credits the payer, and updates net balances.
    show_balances(): Displays current standing balances for all members.
    settle_up(): Computes and displays the optimized list of final transactions.

Author : Dhyani Panchal
      

