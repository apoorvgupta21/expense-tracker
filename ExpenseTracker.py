# Create an expense tracker
# https://roadmap.sh/projects/number-guessing-game

import json
print("\nWelcome to Expense Tracker! \n")

total_expense = 0

class Expense():
    def __init__(self, exp_desc, amount):
        self.exp_desc = exp_desc
        self.amount = amount
        #return self.exp_desc, self.amount
    
    def vals(self):    
        #return self.exp_desc, self.amount
         return {self.exp_desc: self.amount}   
        

exp1 = Expense("Shoes", "Rs 5000")
exp2 = Expense("Grocery", "Rs 700")
exp3 = Expense("OTT", "Rs 4000")

print(exp1.vals())
print(exp2.vals())  

with open("data.json", "w") as outfile:
    json.dump(exp1.vals(), outfile, indent=4)
    json.dump(exp2.vals(), outfile, indent=4)
