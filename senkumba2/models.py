from django.contrib.auth.models import User
from django.db.models import Model, DateField, ForeignKey, CharField, TextField, IntegerField
from django.utils import timezone


class Payment(Model):
    SHARES = 'shares'
    SAVINGS = 'savings'
    FINE = 'fine'
    OPERATIONS = 'operations'
    TYPE_CHOICES = (
        (SHARES, 'Share'),
        (SAVINGS, 'Saving'),
        (FINE, 'Fine'),
        (OPERATIONS, 'Operation'),

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
    comments = TextField()
    date = DateField(blank=True, null=True)
    created = DateField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()

    def _make_payment(self):
        if self.type == self.SHARES:
            shares = Share.objects.get_or_create(user=self.user)[0]
            print(shares.amount)
            shares.amount += self.amount
            shares.save()
        elif self.type == self.SAVINGS:
            savings = Saving.objects.get_or_create(user=self.user)[0]
            savings.amount += self.amount
            savings.save()
        elif self.type == self.OPERATIONS:
            operations = Operation.objects.get_or_create(user=self.user)[0]
            operations.amount += self.amount
            operations.save()
        elif self.type == self.FINE:
            fines = Fine.objects.get_or_create(user=self.user)[0]
            fines.amount += self.amount
            fines.save()

        if self.date == None:
            self.date = timezone.now()
            self.save()

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
        self._make_payment()


class Share(Model):
    user = ForeignKey(User, related_name='shares')
    amount = IntegerField(default=0)

    def __str__(self):
        return self.user.__str__()


class Saving(Model):
    user = ForeignKey(User, related_name='savings')
    amount = IntegerField(default=0)

    def __str__(self):
        return self.user.__str__()


class Fine(Model):
    user = ForeignKey(User, related_name='fines')
    amount = IntegerField(default=0)

    def __str__(self):
        return self.user.__str__()


class Operation(Model):
    user = ForeignKey(User, related_name='operations')
    amount = IntegerField(default=0)

    def __str__(self):
        return self.user.__str__()


def user_new_str(self):
    return self.username if self.get_full_name() == "" else self.get_full_name()


# Replace the __str__ method in the User class with our new implementation
User.__str__ = user_new_str