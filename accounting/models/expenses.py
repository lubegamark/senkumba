"""
Models Dealing with Expenses
"""
from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, IntegerField, DateField, DateTimeField


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
