from rest_framework_json_api import serializers
from .models import Wallet, Transaction

class WalletSerializer(serializers.ModelSerializer):
    class Meta:  # noqa: D106
        model = Wallet
        fields = ('id', 'label', 'balance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:  # noqa: D106
        model = Transaction
        fields = ('id', 'wallet', 'txid', 'amount')
