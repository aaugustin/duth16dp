from django.db import models


class Branch(models.Model):
    id = models.IntegerField(
        db_column='bid',
        primary_key=True,
        verbose_name="ID",
    )
    balance = models.IntegerField(
        blank=True,
        db_column='bbalance',
        null=True,
        verbose_name="balance",
    )
    filler = models.CharField(
        max_length=88,
        blank=True,
        null=True,
        verbose_name="filler",
    )

    class Meta:
        db_table = 'pgbench_branches'
        managed = False
        verbose_name = "branch"
        verbose_name_plural = "branches"

    def __str__(self):
        return '<Branch: {}>'.format(self.pk)


class Account(models.Model):
    id = models.IntegerField(
        db_column='aid',
        primary_key=True,
        verbose_name="ID",
    )
    branch = models.ForeignKey(
        to=Branch,
        on_delete=models.DO_NOTHING,
        db_column='bid',
        blank=True,
        null=True,
        verbose_name="branch",
    )
    balance = models.IntegerField(
        blank=True,
        db_column='abalance',
        null=True,
        verbose_name="account balance",
    )
    filler = models.CharField(
        max_length=84,
        blank=True,
        null=True,
        verbose_name="filler",
    )

    class Meta:
        db_table = 'pgbench_accounts'
        managed = False
        verbose_name = "account"
        verbose_name_plural = "accounts"

    def __str__(self):
        return '<Account: {}>'.format(self.pk)


class Teller(models.Model):
    id = models.IntegerField(
        db_column='tid',
        primary_key=True,
        verbose_name="ID",
    )
    branch = models.ForeignKey(
        to=Branch,
        on_delete=models.DO_NOTHING,
        db_column='bid',
        blank=True,
        null=True,
        verbose_name="branch",
    )
    balance = models.IntegerField(
        blank=True,
        db_column='tbalance',
        null=True,
        verbose_name="teller balance",
    )
    filler = models.CharField(
        max_length=84,
        blank=True,
        null=True,
        verbose_name="filler",
    )

    class Meta:
        db_table = 'pgbench_tellers'
        managed = False
        verbose_name = "teller"
        verbose_name_plural = "tellers"

    def __str__(self):
        return '<Teller: {}>'.format(self.pk)


class Transaction(models.Model):
    id = models.IntegerField(
        db_column='hid',
        primary_key=True,
        verbose_name="ID",
    )
    teller = models.ForeignKey(
        to=Teller,
        on_delete=models.DO_NOTHING,
        db_column='tid',
        blank=True,
        null=True,
        verbose_name="teller",
    )
    branch = models.ForeignKey(
        to=Branch,
        on_delete=models.DO_NOTHING,
        db_column='bid',
        blank=True,
        null=True,
        verbose_name="branch",
    )
    account = models.ForeignKey(
        to=Account,
        on_delete=models.DO_NOTHING,
        db_column='aid',
        blank=True,
        null=True,
        verbose_name="account",
    )
    delta = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="change",
    )
    mtime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="time",
    )
    filler = models.CharField(
        max_length=22,
        blank=True,
        null=True,
        verbose_name="filler",
    )

    class Meta:
        db_table = 'pgbench_history'
        managed = False
        verbose_name = "transaction"
        verbose_name_plural = "transactions"

    def __str__(self):
        return '<Transaction: {}>'.format(self.pk)
