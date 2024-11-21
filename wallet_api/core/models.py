from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=36, decimal_places=18, default=0)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("Wallet balance cannot be negative")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label


class Transaction(models.Model):
    class Meta:  # noqa: D106
        indexes = [
            models.Index(fields=['txid']),
            models.Index(fields=['wallet']),
        ]
    wallet = models.ForeignKey(Wallet, related_name="transactions", on_delete=models.CASCADE)
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)

    def save(self, *args, **kwargs):
        self.wallet.balance += self.amount
        self.wallet.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.txid}"
