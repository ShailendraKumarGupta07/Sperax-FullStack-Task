from rest_framework import serializers
from .models import Wallet, Token, Watchlist, TokenBalance, Transaction, TokenAllowance, HistoricalTokenBalance

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'address', 'created_at']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'name', 'symbol', 'contract_address', 'decimals', 'added_at']

class WatchlistSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    token = TokenSerializer()

    class Meta:
        model = Watchlist
        fields = ['id', 'wallet', 'token', 'added_at']

class TokenBalanceSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    token = TokenSerializer()

    class Meta:
        model = TokenBalance
        fields = ['id', 'wallet', 'token', 'balance', 'date_fetched']

class TransactionSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    token = TokenSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'wallet', 'token', 'recipient_address', 'amount', 'tx_hash', 'timestamp']

class TokenAllowanceSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    token = TokenSerializer()

    class Meta:
        model = TokenAllowance
        fields = ['id', 'wallet', 'token', 'contract_address', 'allowance', 'updated_at']

class HistoricalTokenBalanceSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()
    token = TokenSerializer()

    class Meta:
        model = HistoricalTokenBalance
        fields = ['id', 'wallet', 'token', 'balance', 'date', 'fetched_at']
