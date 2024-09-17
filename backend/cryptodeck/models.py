from django.db import models

class Wallet(models.Model):
    address = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Token(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    contract_address = models.CharField(max_length=255, unique=True)
    decimals = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet} watches {self.token}"

class TokenBalance(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=8)
    date_fetched = models.DateTimeField()

    def __str__(self):
        return f"{self.wallet} has {self.balance} of {self.token}"

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    recipient_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    tx_hash = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Transaction {self.tx_hash}"

class TokenAllowance(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    contract_address = models.CharField(max_length=255)
    allowance = models.DecimalField(max_digits=20, decimal_places=8)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.wallet} allowance for {self.contract_address}"

class HistoricalTokenBalance(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=8)
    date = models.DateField()
    fetched_at = models.DateTimeField()

    def __str__(self):
        return f"Historical balance for {self.wallet} on {self.date}"
