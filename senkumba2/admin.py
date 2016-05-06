from django.contrib import admin
from django.contrib.admin import ModelAdmin

from senkumba2.models import Payment, Share, Saving, Fine, Operation


class PaymentsAdmin(ModelAdmin):
    list_display = ('user', 'type', 'source', 'amount', 'date', 'created','comments', )
    list_filter = ('user','type', 'source')
    ordering = ('-date', '-created')


class SharesAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')


class SavingsAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')


class FinesAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')


class OperationsAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')


admin.site.register(Payment, PaymentsAdmin)
admin.site.register(Share, SharesAdmin)
admin.site.register(Saving, SavingsAdmin)
admin.site.register(Fine, FinesAdmin)
admin.site.register(Operation, OperationsAdmin)
