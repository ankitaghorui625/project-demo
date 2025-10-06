def summarize_by_category(expenses):
    summary={}
    for expense in expenses:
        summary[expense.category]=summary.get(expense.category, 0)+ expense.amount
    return summary