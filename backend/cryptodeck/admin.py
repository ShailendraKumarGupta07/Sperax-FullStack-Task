from django.contrib import admin
from .models import Wallet, Token, Watchlist, TokenBalance, Transaction, TokenAllowance, HistoricalTokenBalance

admin.site.register(Wallet)
admin.site.register(Token)
admin.site.register(Watchlist)
admin.site.register(TokenBalance)
admin.site.register(Transaction)
admin.site.register(TokenAllowance)
admin.site.register(HistoricalTokenBalance)
