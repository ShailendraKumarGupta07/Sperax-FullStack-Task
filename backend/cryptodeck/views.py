from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Wallet, Token, Watchlist, TokenBalance, Transaction, TokenAllowance, HistoricalTokenBalance
from .serializers import WalletSerializer, TokenSerializer, WatchlistSerializer, TokenBalanceSerializer, TransactionSerializer, TokenAllowanceSerializer, HistoricalTokenBalanceSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=False, methods=['get'])
    def by_address(self, request):
        address = request.query_params.get('address')
        wallet = Wallet.objects.get(address=address)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


class TokenBalanceViewSet(viewsets.ModelViewSet):
    queryset = TokenBalance.objects.all()
    serializer_class = TokenBalanceSerializer

    @action(detail=False, methods=['get'])
    def by_wallet(self, request):
        wallet_address = request.query_params.get('wallet')
        balances = TokenBalance.objects.filter(wallet__address=wallet_address)
        serializer = self.get_serializer(balances, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['get'])
    def by_wallet(self, request):
        wallet_address = request.query_params.get('wallet')
        transactions = Transaction.objects.filter(wallet__address=wallet_address)
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)


class TokenAllowanceViewSet(viewsets.ModelViewSet):
    queryset = TokenAllowance.objects.all()
    serializer_class = TokenAllowanceSerializer

    @action(detail=False, methods=['get'])
    def by_wallet(self, request):
        wallet_address = request.query_params.get('wallet')
        allowances = TokenAllowance.objects.filter(wallet__address=wallet_address)
        serializer = self.get_serializer(allowances, many=True)
        return Response(serializer.data)



class HistoricalTokenBalanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalTokenBalance.objects.all()
    serializer_class = HistoricalTokenBalanceSerializer

    @action(detail=False, methods=['get'])
    def by_wallet_and_token(self, request):
        wallet_address = request.query_params.get('wallet')
        token_id = request.query_params.get('token')
        historical_balances = HistoricalTokenBalance.objects.filter(wallet__address=wallet_address, token__id=token_id)
        serializer = self.get_serializer(historical_balances, many=True)
        return Response(serializer.data)
