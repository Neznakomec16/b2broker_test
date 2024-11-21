import pytest
from decimal import Decimal
from django.db.utils import IntegrityError
from core.models import Wallet, Transaction


@pytest.mark.django_db
def test_wallet_creation():
    wallet = Wallet.objects.create(label="Test Wallet")
    assert wallet.label == "Test Wallet"
    assert wallet.balance == Decimal("0.0")


@pytest.mark.django_db
def test_transaction_creation():
    wallet = Wallet.objects.create(label="Test Wallet")
    transaction = Transaction.objects.create(wallet=wallet, txid="unique_txid_123", amount=Decimal("100.0"))
    wallet.refresh_from_db()
    assert transaction.txid == "unique_txid_123"
    assert transaction.amount == Decimal("100.0")
    assert wallet.balance == Decimal("100.0")


@pytest.mark.django_db
def test_negative_balance_transaction():
    wallet = Wallet.objects.create(label="Test Wallet")
    with pytest.raises(ValueError, match="Wallet balance cannot be negative"):
        Transaction.objects.create(wallet=wallet, txid="unique_txid_456", amount=-200.0)
