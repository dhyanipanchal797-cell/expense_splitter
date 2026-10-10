# Expense Splitter
A command-line tool written in Python designed to split group expenses—similar to Splitwise. It calculates individual balances and generates an optimized settlement plan to minimize the number of cash transfers required between roommates or friends.

## Features

1. Dynamic Group Management: Add any number of participants to the expense group.
2. Flexible Expense Splitting: Record who paid and split the amount equally among any subset of participants.
3. Real-time Balance Tracking: View who is owed money, who owes money, and who is fully settled up.
4. Optimized Settlement Algorithm: Automatically matches debtors with creditors to compute the minimum number of transactions needed to clear all debts.
5. Dual Modes: Choose between a pre-loaded sample trip demo or an interactive mode to input your own custom names and expenses.

## Project Structure

```
expense-splitter/
│
├── expense-splitter.py   # Core application script
└── README.md             # Project documentation
```

## Getting Started 

Prerequisites :
1. Python 3.x installed on your system.

Running the Script :
2. Clone or download the script file (expense-splitter.py).
3. Open your terminal or command prompt in the directory containing the file.
4. Run the script using Python: python expense-splitter.py
5. Choose between the Demo Mode (to see a pre-configured sample group) or Interactive Mode (to input your own custom names and expenses).

Code Overview :

1. The script is structured around a core ExpenseSplitter class:
2. add_person(name): Registers a new user into the tracking ledger.
3. add_expense(payer, amount, participants): Deducts shares, credits the payer, and updates net balances.
4. show_balances(): Displays current standing balances for all members.
5. settle_up(): Computes and displays the optimized list of final transactions.

## Author : Dhyani Panchal
      

