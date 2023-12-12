from builtins import range


class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.balance -= amount
        self.ledger.append({
            'amount': -amount,
            'description': description,
        })

        return True

    def transfer(self, amount, other_cat):
        if not self.withdraw(amount, "Transfer to " + other_cat.name):
            return False

        other_cat.deposit(amount, "Transfer from " + self.name)
        return True

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return self.balance >= amount

    def spent(self):
        return -sum(transaction["amount"] for transaction in self.ledger if transaction["amount"] < 0)

    def __str__(self):
        lines = [self.name.center(30, "*")]
        for transaction in self.ledger:
            description = transaction["description"][:23]
            lines.append("{:<23}{:>7.2f}".format(description, transaction["amount"]))

        lines.append("Total: {}".format(self.balance))
        return "\n".join(lines)


def create_spend_chart(categories):
    spending = [c.spent() for c in categories]
    total = sum(spending)
    percentages = [s * 100 / total for s in spending]
    ss = ["Percentage spent by category"]
    for i in range(0, 11):
        level = 10 * (10 - i)
        s = '{:>3}| '.format(level)
        for p in percentages:
            if p >= level:
                s += "o  "
            else:
                s += "   "
        ss.append(s)
    padding = " " * 4
    ss.append(padding + "-" * 3 * len(spending) + "-")

    names = [c.name for c in categories]
    n = max(map(len, names))
    for i in range(0, n):
        s = padding
        for name in names:
            s += " "
            s += name[i] if len(name) > i else " "
            s += " "

        ss.append(s + " ")

    return "\n".join(ss)