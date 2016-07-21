from django.contrib import admin
from django.contrib.admin import ModelAdmin

from loans.models import LoanApplication, Loan, LoanCategory, InterestType, Period, LoanApplicationStatus, \
    LoanStatus, LoanPayment


class LoansAdmin(ModelAdmin):
    list_display = ('id', 'user', 'start', 'expected_end', 'end', 'type', 'amount', 'status', 'approval_date')
    ordering = ('-approval_date', '-created', 'id')
    search_fields = ('date', 'user', 'type')


class LoanApplicationsAdmin(ModelAdmin):
    list_display = ('id', 'user', 'proposed_start', 'proposed_end', 'type', 'proposed_amount', 'status', 'approved')
    ordering = ('-application_date', '-created', 'id')
    search_fields = ('date', 'user', 'type')


admin.site.register(Loan, LoansAdmin)
admin.site.register(LoanApplication, LoanApplicationsAdmin)
admin.site.register(LoanCategory)
admin.site.register(LoanStatus)
admin.site.register(LoanApplicationStatus)
admin.site.register(LoanPayment)
admin.site.register(Period)
admin.site.register(InterestType)
