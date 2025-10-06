class Expense:
    def __init__(self, amount, category, date):
        self.amount=amount
        self.category=category
        self.date=date
        
    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount}"

    def to_dict(self):
        return {"amount": self.amount, "category":self.category, "date":self.date}
    
    def from_dict(data):
        return Expense(data["amount"], data["category"], data["date"])