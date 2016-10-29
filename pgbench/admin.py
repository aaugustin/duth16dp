from django.contrib import admin

from . import models


@admin.register(models.Branch)
class Branch(admin.ModelAdmin):
    list_display = ['id', 'balance']


@admin.register(models.Account)
class Account(admin.ModelAdmin):
    list_display = ['id', 'branch', 'balance']


@admin.register(models.Teller)
class Teller(admin.ModelAdmin):
    list_display = ['id', 'branch', 'balance']


@admin.register(models.Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ['id', 'teller', 'branch', 'account', 'delta', 'mtime']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('teller', 'branch', 'account')
