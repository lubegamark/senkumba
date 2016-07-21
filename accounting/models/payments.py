"""
Models Dealing with Payments
"""
from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CharField, IntegerField, TextField, DateField, DateTimeField
from django.utils import timezone


class Payment(Model):
    SHARES = 'shares'
    SAVINGS = 'savings'
    FINE = 'fine'
    OPERATIONS = 'operations'
    REGISTRATION = 'registration'
    OTHER = 'other'
    TYPE_CHOICES = (
        (SHARES, 'Share'),
        (SAVINGS, 'Saving'),
        (FINE, 'Fine'),
        (OPERATIONS, 'Operation'),
        (REGISTRATION, 'Registration'),
        (OTHER, 'Other'),

    )
    CASH = 'cash'
    MM = 'mobile_money'
    SOURCE_CHOICES = (
        (CASH, 'Cash'),
        (MM, 'Mobile Money'),
    )
    user = ForeignKey(User, related_name='payments')
    type = CharField(max_length=50, choices=TYPE_CHOICES)
    source = CharField(max_length=50, choices=SOURCE_CHOICES)
    amount = IntegerField()
    comments = TextField(blank=True, null=True)
    date = DateField()
    start = DateField(blank=True, null=True)
    end = DateField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()

    def period(self):

        return self.start.strftime("%b %Y") if self.start else None

    def _make_payment(self):
        if self.date is None:
            self.date = timezone.now()
            self.save()

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
        self._make_payment()
