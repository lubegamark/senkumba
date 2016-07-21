from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db.models import Sum

from accounting.models import Payment
from accounting.models import Expense


class PaymentsAdmin(ModelAdmin):
    list_display = ('id', 'user', 'type',  'source', 'amount', 'date', 'period', 'comments',)
    list_filter = ('user', 'type', 'created', 'source', 'date',)
    ordering = ('-date', '-created', 'id', 'user',)
    search_fields = ('date', 'user')
    list_display_links = ('user',)


class ExpensesAdmin(ModelAdmin):
    list_display = ('id', 'user', 'type', 'amount', 'date', 'comments', 'created',)
    list_filter = ('user','type', 'created', 'date', )
    ordering = ('-date', '-created', 'id')
    search_fields = ('date', 'user')


class SharesSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Shares'
        verbose_name_plural = 'Shares'


class SharesAdmin(ModelAdmin):
    list_display = ('__str__', 'total_shares',)

    def get_queryset(self, request):
        qs = super(SharesAdmin, self).get_queryset(request)
        return qs.filter(payments__type=Payment.SHARES)\
            .annotate(total_shares=Sum('payments__amount'))\
            .order_by('-total_shares')

    def total_shares(self, obj):
        return obj.total_shares
    total_shares.short_description = 'Total Shares'


class SavingsSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Savings'
        verbose_name_plural = 'Savings'


class SavingsAdmin(ModelAdmin):
    list_display = ('__str__', 'total_savings',)

    def get_queryset(self, request):
        qs = super(SavingsAdmin, self).get_queryset(request)
        return qs.filter(payments__type=Payment.SAVINGS)\
            .annotate(total_savings=Sum('payments__amount'))\
            .order_by('-total_savings')

    def total_savings(self, obj):
        return obj.total_savings
    total_savings.short_description = 'Total Savings'


class FinesSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Fines'
        verbose_name_plural = 'Fines'


class FinesAdmin(ModelAdmin):
    list_display = ('__str__', 'total_fines',)

    def get_queryset(self, request):
        qs = super(FinesAdmin, self).get_queryset(request)
        return qs.filter(payments__type=Payment.FINE)\
            .annotate(total_fines=Sum('payments__amount'))\
            .order_by('-total_fines')

    def total_fines(self, obj):
        return obj.total_fines
    total_fines.short_description = 'Total Fines'


class OperationsSummary(User):
    class Meta:
        proxy = True
        verbose_name = 'Operations'
        verbose_name_plural = 'Operations'


class OperationsAdmin(ModelAdmin):
    list_display = ('__str__', 'total_operations',)

    def get_queryset(self, request):
        qs = super(OperationsAdmin, self).get_queryset(request)
        return qs.filter(payments__type=Payment.OPERATIONS)\
            .annotate(total_operations=Sum('payments__amount'))\
            .order_by('-total_operations')

    def total_operations(self, obj):
        return obj.total_operations
    total_operations.short_description = 'Total Operations'


admin.site.register(Payment, PaymentsAdmin)
admin.site.register(Expense, ExpensesAdmin)
admin.site.register(SharesSummary, SharesAdmin)
admin.site.register(SavingsSummary, SavingsAdmin)
admin.site.register(FinesSummary, FinesAdmin)
admin.site.register(OperationsSummary, OperationsAdmin)

