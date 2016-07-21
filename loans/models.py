"""
Models Dealing with Loans
"""

from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, IntegerField, ForeignKey, ManyToManyField, BooleanField, \
    DateTimeField, FloatField, DateField, OneToOneField


class LoanCategory(Model):
    name = CharField(max_length=255)
    description = TextField()

    class Meta:
        verbose_name_plural = 'Loan Categories'

    def __str__(self):
        return self.name


class LoanApplicationStatus(Model):
    name = CharField(max_length=255)
    description = TextField()

    class Meta:
        verbose_name_plural = 'Loan Application Statuses'

    def __str__(self):
        return self.name


class LoanStatus(Model):
    name = CharField(max_length=255)
    description = TextField()

    class Meta:
        verbose_name_plural = 'Loan Statuses'

    def __str__(self):
        return self.name


class Period(Model):
    """
    Intervals used to measure interest periods and their definitions in days
    For example "Month - 30days"
    """
    name = CharField(max_length=255)
    days = IntegerField()

    def __str__(self):
        return self.name


class InterestType(Model):
    name = CharField(max_length=255)
    period = ForeignKey(Period)
    description = TextField()

    def __str__(self):
        return self.name


class LoanApplication(Model):
    """
    A Loan application is made by a user. When approved, a Loan is created based on the application.
    """
    user = ForeignKey(User, related_name='loan_applications')
    type = ForeignKey(LoanCategory)
    comments = TextField(blank=True, null=True)
    guaranteed_by = ManyToManyField(User, blank=True, related_name='loan_applications_guaranteed')
    application_date = DateField()
    proposed_amount = IntegerField()
    proposed_start = DateField()
    proposed_end = DateField()
    status = ForeignKey(LoanApplicationStatus)
    approved = BooleanField()
    approved_by = ManyToManyField(User, blank=True, related_name='loans_approved')
    approved_at = DateField(blank=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} at {1}".format(self.user.__str__(), self.application_date)


class Loan(Model):
    """
    A Loan is created when a LoanApplication is approved.
    """
    loan_application = OneToOneField(LoanApplication, related_name='loan')
    user = ForeignKey(User, related_name='loans')
    type = ForeignKey(LoanCategory)
    comments = TextField(blank=True, null=True)
    approval_date = DateField()
    interest = FloatField()
    interest_type = ForeignKey(InterestType, related_name='loans')
    guaranteed_by = ManyToManyField(User, blank=True, related_name='loans_guaranteed')
    amount = IntegerField(blank=True, null=True)
    start = DateField(blank=True, null=True)
    expected_end = DateField()
    end = DateField(blank=True, null=True)
    status = ForeignKey(LoanStatus)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} Loan #{1}".format(self.user.__str__(), self.id)


class LoanPayment(Model):
    """
    Payment made against a loan
    """
    date = DateField()
    user = ForeignKey(User, related_name='loan_payments')
    loan = ForeignKey(Loan, related_name='payments')
    amount = IntegerField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.user.__str__(), self.loan, self.date)
