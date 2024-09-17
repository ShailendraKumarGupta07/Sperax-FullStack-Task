from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, TokenViewSet, WatchlistViewSet, TokenBalanceViewSet, TransactionViewSet, TokenAllowanceViewSet, HistoricalTokenBalanceViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'tokens', TokenViewSet)
router.register(r'watchlists', WatchlistViewSet)
router.register(r'balances', TokenBalanceViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'allowances', TokenAllowanceViewSet)
router.register(r'historical_balances', HistoricalTokenBalanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
