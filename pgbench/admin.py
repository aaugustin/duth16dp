from django.contrib import admin

from . import models


@admin.register(models.Branch)
class Branch(admin.ModelAdmin):
    list_display = ['id', 'balance']


@admin.register(models.Account)
class Account(admin.ModelAdmin):
    list_display = ['id', 'branch', 'balance', 'transactions']
    list_select_related = ['branch']

    def transactions(self, account):
        transactions = account.transaction_set.all()
        return ', '.join(str(transaction.delta) for transaction in transactions)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(Prefetch(
            'transaction_set', models.Transaction.objects.order_by('-mtime')))


@admin.register(models.Teller)
class Teller(admin.ModelAdmin):
    list_display = ['id', 'branch', 'balance']


@admin.register(models.Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ['id', 'teller', 'branch', 'account', 'delta', 'mtime']
    list_select_related = ['teller', 'branch', 'account']
