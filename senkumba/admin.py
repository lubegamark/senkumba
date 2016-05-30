from django.contrib import admin
from django.contrib.admin import ModelAdmin

from senkumba.models import Payment, Share, Saving, Fine, Operation, Other, Registration


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


class RegistrationAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')


class OthersAdmin(ModelAdmin):
    list_display = ('user', 'amount',)
    readonly_fields = ('user', 'amount')
admin.site.register(Payment, PaymentsAdmin)
admin.site.register(Share, SharesAdmin)
admin.site.register(Saving, SavingsAdmin)
admin.site.register(Fine, FinesAdmin)
admin.site.register(Operation, OperationsAdmin)
admin.site.register(Other, OthersAdmin)
admin.site.register(Registration, RegistrationAdmin)
