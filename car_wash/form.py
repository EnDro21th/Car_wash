from .models import *
from django.forms import ModelForm


class ImportForm(ModelForm):
    class Meta:
        model = Import
        fields = '__all__'


class ImportdetailForm(ModelForm):
    class Meta:
        model = Importdetail
        fields = '__all__'


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class ExpensedetailForm(ModelForm):
    class Meta:
        model = Expensedetail
        fields = '__all__'
