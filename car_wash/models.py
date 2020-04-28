from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    catid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    catname = models.CharField(max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.catname


class Stock(models.Model):
    productid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    productname = models.CharField(max_length=255)  # Field name made lowercase.
    qty = models.IntegerField()  # Field name made lowercase.
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)  # Field name made lowercase.a
    cost = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    unitprice = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    onhand = models.IntegerField(blank=True)  # Field name made lowercase.
    reorder = models.IntegerField(blank=True)  # Field name made lowercase.
    vat = models.DecimalField(max_digits=3, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return self.productname


class Customer(models.Model):
    cid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    cphonenumber = models.CharField(max_length=10)  # Field name made lowercase.
    count = models.IntegerField(blank=True, default='1')  # Field name made lowercase.
    total_count = models.IntegerField(blank=True, default='1')  # Field name made lowercase.
    limit = models.IntegerField(blank=True, null=True, default=10)
    lastdate = models.DateField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.cphonenumber)


class Expense(models.Model):
    exid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    sid = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    appby = models.CharField(max_length=255, default='admin', blank=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.exid)


class Expensetype(models.Model):
    extypeid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    extypename = models.CharField(max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.extypename


class Expensedetail(models.Model):
    exdid = models.BigAutoField(primary_key=True)
    exid = models.ForeignKey(Expense, on_delete=models.CASCADE)  # Field name made lowercase.
    extypeid = models.ForeignKey(Expensetype, on_delete=models.CASCADE)  # Field name made lowercase.
    desciption = models.CharField(max_length=255)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    qty = models.IntegerField()  # Field name made lowercase.

    def __str__(self):
        return str(self.exdid)


class Supplier(models.Model):
    suppid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    supptel = models.CharField(max_length=255)  # Field name made lowercase.
    suppname = models.CharField(max_length=255)  # Field name made lowercase.
    suppaddress = models.CharField(max_length=255, blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.suppname


class Import(models.Model):
    importid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(auto_now=False, auto_now_add=False)  # Field name made lowercase.
    sid = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    discount_total = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    grand_total = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True)  # Field name made lowercase.
    suppid = models.ForeignKey(Supplier, on_delete=models.CASCADE)  # Field name made lowercase.
    billno = models.CharField(max_length=30, blank=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.importid)


class Importdetail(models.Model):
    importdetailid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    importid = models.ForeignKey(Import, on_delete=models.CASCADE)  # Field name made lowercase.
    productid = models.ForeignKey(Stock, on_delete=models.CASCADE)  # Field name made lowercase.
    qty = models.IntegerField()  # Field name made lowercase.
    cost = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.importdetailid)


class Sell(models.Model):
    sellid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(auto_now=False, auto_now_add=False)  # Field name made lowercase.
    sid = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Field name made lowercase.
    vat = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grant_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)  # Field name made lowercase.

    def __str__(self):
        return str(self.sellid)


class Selldetail(models.Model):
    selldetailid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Stock, on_delete=models.CASCADE)  # Field name made lowercase.
    sellid = models.ForeignKey(Sell, on_delete=models.CASCADE)  # Field name made lowercase.
    qty = models.IntegerField()  # Field name made lowercase.
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # Field name made lowercase.
    discount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.selldetailid)


class Ajustment(models.Model):
    ajid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    sid = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.
    appby = models.CharField(max_length=255, default='admin', blank=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.ajid)


class Ajustmentdetal(models.Model):
    ajdid = models.BigAutoField(primary_key=True)  # Field name made lowercase.
    ajid = models.ForeignKey(Ajustment, on_delete=models.CASCADE)  # Field name made lowercase.
    productid = models.ForeignKey(Stock, on_delete=models.CASCADE)  # Field name made lowercase.
    description = models.CharField(max_length=255)  # Field name made lowercase.
    qty = models.IntegerField(default=0)  # Field name made lowercase.
    brokenprice = models.DecimalField(max_digits=8, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return str(self.ajdid)
