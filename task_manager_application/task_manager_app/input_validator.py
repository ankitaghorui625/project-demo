import re
def validate_string_input(prompt, pattern=None):
    value=input(prompt).strip()
    if pattern and not re.match(pattern, value):
        print("Invalid format. Please use letters and spaces only.")
        return None
    return value
def validate_priority():
    while True:
        priority=input("Enter priority (high / medium / low) : ").strip().capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Please enter high, medium or low")
            print("Task creation failed")
            return None
        else:
            return priority
    
   