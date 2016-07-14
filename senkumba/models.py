from django.contrib.auth.models import User
from django.db.models import Model, DateField, ForeignKey, CharField, TextField, IntegerField, DateTimeField, Sum, \
    ManyToManyField, FloatField, BooleanField
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
        if self.date == None:
            self.date = timezone.now()
            self.save()

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
        self._make_payment()


class ExpenseCategory(Model):
    name = CharField(max_length=255)
    description = TextField()

    def __str__(self):
        return self.name


class Expense(Model):
    user = ForeignKey(User, related_name='expenses')
    type = ForeignKey('ExpenseCategory', )
    amount = IntegerField()
    comments = TextField(blank=True, null=True)
    date = DateField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()


class LoanCategory(Model):
    name = CharField(max_length=255)
    description = TextField()

    def __str__(self):
        return self.name


class Loan(Model):
    user = ForeignKey(User, related_name='loans')
    type = ForeignKey('LoanCategory', )
    amount = IntegerField()
    comments = TextField(blank=True, null=True)
    date = DateField()
    start = DateField()
    end = DateField()
    interest = FloatField(help_text='per month')
    guaranteed_by = ManyToManyField(User, null=True, blank=True, related_name='loans_guaranteed')
    approved_by = ManyToManyField(User, 'loans_approved')
    approved = BooleanField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()


def user_new_str(self):
    return self.username if self.get_full_name() == "" else self.get_full_name()


# Replace the __str__ method in the User class with our new implementation
User.__str__ = user_new_str