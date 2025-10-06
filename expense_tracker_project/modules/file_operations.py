import json
import os
from modules.expense import Expense
FILE_PATH="data/expenses.txt"
def save_expenses(expenses):
    with open(FILE_PATH, "w") as f:
        json.dump([e.to_dict()for e in expenses], f, indent=4)
def load_expenses():
    if not os.path.exists(FILE_PATH):
        return[]
    with open(FILE_PATH, "r") as f:
       try:
         data=json.load(f)
         return [Expense.from_dict(d) for d in data]
       except json.JSONDecodeError :
           return[]  

