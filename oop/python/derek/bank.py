# Design a simple banking system. It needs to be able

# -Bank
# -Create account
#   -If already there error out
# -Deposit to account (including adding and removing)
#   -If not enough funds then error out
# -Transfer from one account to another (remember to block if not enough money and shit)
#   -If account doesn't exist error out
#   -If not enough funds error out
# -Find n acounts with the most transaction amount (negative and positive are both transaction amounts)
#   -Return by transaction first and then if they are the same amount alphabetical


class Account:

  def __init__(self, acc_name: str) -> None:
    self.total = 0
    self.transactions = 0
    self.name = acc_name

  def deposit(self, amount: int):
    if (amount < 0):
      if (abs(amount) > self.total):
        raise Exception(f"ERROR: Cannot deduct {abs(amount)} from the account {self.name}")
    self.total += amount
    self.transactions += abs(amount)

  def __repr__(self) -> str:
    return f"name: {self.name}, total: {self.total}, transactions: {self.transactions}"

class Bank:

  def __init__(self) -> None:
    self.accounts = {}

  def create_account(self, acc_name: str) -> None:
    if (acc_name in self.accounts):
      raise Exception(f"The account {acc_name} already exists.")
    self.accounts[acc_name] = Account(acc_name=acc_name)

  def deposit(self, acc_name: str, amount: int) -> None:
    if (acc_name not in self.accounts):
      raise Exception(f"The account {acc_name} does not exist")
    self.accounts[acc_name].deposit(amount)

  def transfer(self, acc1: str, acc2: str, amount: int) -> None:
    if (acc1 not in self.accounts):
      raise Exception(f"The account {acc1} does not exist")
    if (acc2 not in self.accounts):
      raise Exception(f"The account {acc2} does not exist")
    
    # remove from the first account
    # This throws an exception if there are not enough funds
    self.accounts[acc1].deposit(-amount)
    # add to the second account
    self.accounts[acc2].deposit(amount)

  def mostActiveAccounts(self, n: int):
    return sorted(self.accounts.values(), key=lambda acc: (-acc.transactions, acc.name))[:n]


  def __repr__(self) -> str:
    accounts_info = [
      {acc_name: {"total": acc.total, "transactions": acc.transactions}}
      for acc_name, acc in self.accounts.items()
    ]
    return str(accounts_info)
    

inputs = [
    ["CREATE_ACCOUNT", "acc1"],
    ["DEPOSIT", "acc1", 500],
    ["CREATE_ACCOUNT", "acc2"],
    ["DEPOSIT", "acc2", 200],
    ["TRANSFER", "acc1", "acc2", 100],
    ["TRANSFER", "acc1", "acc3", 600],  # Error: destination account does not exist
    ["CREATE_ACCOUNT", "acc3"],
    ["DEPOSIT", "acc3", 700],
    ["TRANSFER", "acc3", "acc1", 800],  # Error: not enough funds
    ["DEPOSIT", "acc1", -100],  # Withdraw funds from acc1
    ["DEPOSIT", "acc2", -50],   # Withdraw funds from acc2
    ["TRANSFER", "acc1", "acc2", 300],
    ["TRANSFER", "acc2", "acc1", 150],
    ["CREATE_ACCOUNT", "acc4"],
    ["DEPOSIT", "acc4", 400],
    ["TRANSFER", "acc3", "acc4", 100],
    ["TRANSFER", "acc4", "acc3", 50],
    ["TOP_TRANSACTIONS", 5],
    ["CREATE_ACCOUNT", "acc5"],
    ["DEPOSIT", "acc5", 1000],
    ["TRANSFER", "acc5", "acc4", 500],
    ["TRANSFER", "acc4", "acc5", 250],
    ["DEPOSIT", "acc4", -150],  # Withdraw funds from acc4
    ["CREATE_ACCOUNT", "acc6"],
    ["DEPOSIT", "acc6", 50],
    ["TRANSFER", "acc6", "acc5", 100],  # Error: not enough funds
    ["DEPOSIT", "acc6", 200],
    ["TRANSFER", "acc6", "acc5", 250],  # Error: not enough funds
    ["TRANSFER", "acc5", "acc6", 300],
    ["TOP_TRANSACTIONS", 3],
    ["CREATE_ACCOUNT", "acc7"],
    ["DEPOSIT", "acc7", 100],
    ["TRANSFER", "acc7", "acc6", 50],
    ["DEPOSIT", "acc7", -20],   # Withdraw funds from acc7
    ["TRANSFER", "acc7", "acc1", 50],
    ["CREATE_ACCOUNT", "acc8"],
    ["TRANSFER", "acc7", "acc8", 30],
    ["TRANSFER", "acc8", "acc7", 10],
    ["TRANSFER", "acc8", "acc7", 50],   # Error: not enough funds
    ["TOP_TRANSACTIONS", 10],
    ["CREATE_ACCOUNT", "acc9"],
    ["TRANSFER", "acc8", "acc9", 50],
    ["TRANSFER", "acc9", "acc8", 25],
    ["CREATE_ACCOUNT", "acc10"],
    ["DEPOSIT", "acc10", 600],
    ["TRANSFER", "acc10", "acc9", 300],
    ["TRANSFER", "acc9", "acc10", 50],
    ["TOP_TRANSACTIONS", 15],
    ["DEPOSIT", "acc11", 100],  # Error: account does not exist
    ["CREATE_ACCOUNT", "acc11"],
    ["DEPOSIT", "acc11", 300],
    ["TRANSFER", "acc11", "acc10", 100],
    ["CREATE_ACCOUNT", "acc12"],
    ["DEPOSIT", "acc12", 400],
    ["TRANSFER", "acc12", "acc11", 200],
    ["TRANSFER", "acc11", "acc12", 50],
    ["TOP_TRANSACTIONS", 3]
]



bank = Bank()

if __name__ == "__main__":
  for input in inputs:
    try:
      if (input[0] == "CREATE_ACCOUNT"):
        bank.create_account(input[1])
      elif (input[0] == "DEPOSIT"):
        bank.deposit(input[1], input[2])
      elif (input[0] == "TRANSFER"):
        bank.transfer(input[1], input[2], input[3])
      elif (input[0] == "TOP_TRANSACTIONS"):
        top = bank.mostActiveAccounts(input[1])
        print(top)
        print('\n\n')
    except Exception as e:
      print(f"Error: {e}")

# print(bank)