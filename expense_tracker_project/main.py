import re
from modules.expense import Expense
from modules.file_operations import save_expenses, load_expenses
from modules.category_summarizer import summarize_by_category

FILE_PATH="data/expenses.txt"

def validate_date(date_string):
   date_pattern=r"^\d{4}-\d{2}-\d{2}$"
   return re.match(date_pattern, date_string)

def display_menu():
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Summarize  by Category")
    print("4.Exit")

def main():
    expenses=load_expenses()
    while True:
        display_menu()
        choice=input("enter your choice: ").strip()
        if choice=="1":
            try:
             amount=float(input("enter amount : "))
             category=input("enter product category : ")
             date=input("enter date(YYYY-MM-DD) : ")
             
             if not validate_date(date):
                print("Invalid date. please enter date in proper format(YYYY-MM-DD)")
                continue
             expense = Expense(amount, category, date)
             expenses.append(expense)
             save_expenses(expenses)
             print("Expense added successfully")
            except ValueError:
               print("amount must be a number")
        elif choice=="2":
             if not expenses:
                print("No expense added yet")
             else:
                print("Date     Category    Amount")
                print("-----    --------    -------")
                for e in expenses:
                 print(e)
        elif choice=="3":
           summary=summarize_by_category(expenses)
           if not summary:
              print("No expenses added")
           else:
              print("\nsummarize by category")
              print("Category    Amount")
              print("---------   --------")
              for catagory, total in summary.items():
                 print(f"{catagory} : ${total}")
        elif choice=="4":
           print("Exiting expense tracker.....")
           break
        else:
           print("Invalid choice...")
if __name__=="__main__":
   main()
           
    