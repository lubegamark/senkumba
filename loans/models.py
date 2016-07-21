"""
Models Dealing with Loans
"""
from datetime import timedelta

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
    SIMPLE = 'simple'
    COMPOUND = 'compound'
    TYPE_CHOICES = (
        (SIMPLE, 'Simple'),
        (COMPOUND, 'Compound')
    )
    name = CharField(max_length=255)
    period = ForeignKey(Period)
    type = CharField(max_length=255, choices=TYPE_CHOICES)
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
    interest_rate = FloatField()
    interest_type = ForeignKey(InterestType, related_name='loans')
    time = IntegerField()
    guaranteed_by = ManyToManyField(User, blank=True, related_name='loans_guaranteed')
    amount = IntegerField()
    start = DateField()
    end = DateField(blank=True, null=True)
    status = ForeignKey(LoanStatus)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} Loan #{1}".format(self.user.__str__(), self.id)

    def total_amount(self):
        return self.amount+self.interest_amount()

    def principal(self):
        return self.amount

    def interest_amount(self):
        if self.interest_type.type == InterestType.SIMPLE:
            return self.amount*(self.interest_rate/100)*self.time
        else:
            #TODO implement Compound Interest
            return self.amount*(self.interest_rate/100)*self.time

    def expected_end(self):
        time_in_days = self.time*self.interest_type.period.days
        return self.start + timedelta(days=time_in_days)

    def summary(self):
        return """Amount:         {0}
        Principal:      {1}
        Interest amount:{2}
        Interest rate:  {3}% per {5}
        Time:           {4} {5}s
        Expected end:   {6}
        """.format(self.total_amount(), self.amount, self.interest_amount(), self.interest_rate, self.time,
                   self.interest_type.period, self.expected_end())


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
