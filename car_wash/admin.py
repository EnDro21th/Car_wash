from django.contrib import admin
from .models import *

admin.site.site_header = "Admin Controller"


# Register your models here.
class InlineAjustment(admin.TabularInline):
    model = Ajustmentdetal
    extra = 1


class AjustmentAdmin(admin.ModelAdmin):
    inlines = [InlineAjustment]
    list_display = ('ajid', 'date', 'sid', 'total', 'appby')
    ordering = ('ajid',)
    search_fields = ('ajid',)


admin.site.register(Ajustment, AjustmentAdmin)


# class AjustmentdetalAdmin(admin.ModelAdmin):
#     list_display = ('ajdid', 'ajid', 'productid', 'description', 'qty', 'brokenprice')
#     ordering = ('ajid',)
#     search_fields = ('ajid',)
#
#
# admin.site.register(Ajustmentdetal, AjustmentdetalAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catid', 'catname')
    ordering = ('catname',)
    search_fields = ('catname',)


admin.site.register(Category, CategoryAdmin)



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cphonenumber', 'count', 'lastdate')
    ordering = ('cid',)
    search_fields = ('cphonenumber', 'cid')


admin.site.register(Customer, CustomerAdmin)


class InlineExpense(admin.TabularInline):
    model = Expensedetail
    extra = 1


class ExpenseAdmin(admin.ModelAdmin):
    inlines = [InlineExpense]
    list_display = ('exid', 'sid', 'date', 'total', 'appby')
    ordering = ('exid',)
    search_fields = ('exid',)


admin.site.register(Expense, ExpenseAdmin)


# class ExpensedetailAdmin(admin.ModelAdmin):
#     list_display = ('exdid', 'exid', 'extypeid', 'desciption', 'cost', 'qty')
#     ordering = ('exdid',)
#     search_fields = ('exdid', 'exid')
#
#
# admin.site.register(Expensedetail, ExpensedetailAdmin)


class ExpensetypeAdmin(admin.ModelAdmin):
    list_display = ('extypeid', 'extypename')
    ordering = ('extypeid',)
    search_fields = ('extypename', 'extypeid',)


admin.site.register(Expensetype, ExpensetypeAdmin)


class InlineImport(admin.TabularInline):
    model = Importdetail
    extra = 1


class ImportAdmin(admin.ModelAdmin):
    inlines = [InlineImport]
    list_display = ('importid', 'date', 'sid', 'discount_total', 'grand_total', 'status', 'suppid', 'billno')
    ordering = ('importid',)
    search_fields = ('importid',)


admin.site.register(Import, ImportAdmin)


# class ImportdetailAdmin(admin.ModelAdmin):
#     list_display = ('importdetailid', 'importid', 'productid', 'qty', 'cost', 'discount', 'total', 'sizeid', 'vat')
#     ordering = ('importdetailid',)
#     search_fields = ('importdetailid', 'importid')
#
#
# admin.site.register(Importdetail, ImportdetailAdmin)


class InlineSell(admin.TabularInline):
    model = Selldetail
    extra = 1


class SellAdmin(admin.ModelAdmin):
    inlines = [InlineSell]
    list_display = ('sellid', 'date', 'sid', 'cid', 'vat', 'discount_total', 'grant_total', 'status')
    ordering = ('sellid',)
    search_fields = ('sellid', 'status')


admin.site.register(Sell, SellAdmin)


# class SelldetailAdmin(admin.ModelAdmin):
#     list_display = ('selldetailid', 'productid', 'sellid', 'qty', 'price', 'discount', 'total')
#     ordering = ('selldetailid',)
#     search_fields = ('selldetailid', 'sellid')
#
#
# admin.site.register(Selldetail, SelldetailAdmin)


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'productid', 'productname', 'qty', 'catid', 'cost', 'unitprice', 'onhand', 'reorder')
    ordering = ('productid',)
    search_fields = ('productid', 'productname', 'reorder')


admin.site.register(Stock, StockAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('suppid', 'supptel', 'suppname', 'suppaddress')
    ordering = ('suppid',)
    search_fields = ('suppname', 'suppid')


admin.site.register(Supplier, SupplierAdmin)

