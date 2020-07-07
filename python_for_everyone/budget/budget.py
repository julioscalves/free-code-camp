class Category:    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        string = f'{self.category:*^30}\n'

        for item in self.ledger:            
            amount_max_len = slice(0, 7, None)
            desc_max_len = slice(0, 23, None)

            amount = float(str(item["amount"])[amount_max_len])
            description = item["description"][desc_max_len]   

            string += f'{description:<23}{item["amount"]:>7.2f}\n'

        total = self.get_balance()
        string += f'Total: {total}'

        return string        

    def operator(self, amount, description=""):
        self.ledger.append({
            "amount"     : amount,
            "description": description
        })

    def deposit(self, amount, description=""):
        self.operator(amount, description)
    
    def withdraw(self, amount, description=""):
        balance = self.get_balance()  

        if self.check_funds(amount):
            self.operator(-amount, description)
            return True

        return False

    def get_balance(self):
        total = 0

        for entry in self.ledger:
            total += entry['amount']

        return total

    def check_funds(self, amount):
        balance = self.get_balance()
        return amount <= balance

    def transfer(self, amount, target):

        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {target.category}')
            target.deposit(amount, f'Transfer from {self.category}')            
            return True   

        return False

def get_spent_value(categories):
    spent = 0
    total = 0
    cat = {}
    
    for category in categories:
        for operation in category.ledger:
            if operation['amount'] < 0:
                spent += operation['amount']
                total += spent
                
        cat[category.category] = spent
        spent = 0

    return cat, total

def create_spend_chart(categories):
    spent_on, total = get_spent_value(categories)
    proportion = {
        category: ((proportion/total)*100) 
            for category, proportion 
                in zip(spent_on.keys(), spent_on.values()) 
    }

    string = '    Percentage spent by category\n'
    
    for index in range(100, -10, -10):
        string += f'{index:>3}|'
        for category, amount in proportion.items():
            if amount >= index:
                string += f'{"o":^3}'
            else:
                string += f'{" "*3:^3}'
        string += '\n'

    string += f'{"-"*10:>14}\n'

    names = list(proportion.keys())
    longest = max(names, key=len)
    bars = ''
    
    for index in range(len(longest) + 1):
        bars += "    "
        for name in names:
            if index < len(name):
                bars += f' {name[index]} '
            else:
                bars += '   '
        bars += "\n"

    string += bars
    return string
