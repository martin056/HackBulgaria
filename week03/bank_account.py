class BankAccount():

    def __init__(self, name, balance, currency):
        self._name = name
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Balance cannot be less than zero.")
        self._currency = currency
        self.history_list = ["Account was created"]

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self._name, self._balance, self._currency)

    def __int__(self):
        self.history_list.append("__int__ check -> {}{}".format(self._balance, self._currency))
        return self._balance

    def __eq__(self, other):
        return self._currency == other._currency

    def __hash__(self):
        return hash(self._name)

    def deposit(self, amount):
        self.history_list.append("Deposited {}{}".format(amount, self._currency))
        self._balance += amount
        if amount <= 0:
            raise ValueError("Deposit must be possitive.")

    def balance(self):
        self.history_list.append("Balance check -> {}{}".format(self._balance, self._currency))
        #return str(self._balance) + self._currency
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            self.history_list.append("Withdraw for {}{} failed".format(amount, self._currency))
            return False

        else:
            self._balance -= amount

            self.history_list.append ("{}{} withdrawed".format(amount, self._currency))
            self.history_list.append ("Balance check -> {}{}".format(self._balance, self._currency))

            return True

    def transfer_to(self, account, amount):
        if self == account:
            self.withdraw(amount)
            account.deposit(amount)
            return True

        else:
            print("TRANSFER FAILURE!!!")
            return False

    def history(self):
        return self.history_list
