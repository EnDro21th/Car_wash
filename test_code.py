# import pandas as pd
#
# # page = 'C:\\Users\\EnDro\\Desktop\\SA\\templates\\page1.html'
# # page = 'http://127.0.0.1:8000/main/'
# # page = 'https://www.w3schools.com/html/html_tables.asp'
# # data_table = pd.read_html(page, attrs={"id": "customers"}, )
# # data_table = pd.read_html(page, attrs={"id": "table_import"}, )
#
# page = 'file:///C:/Users/EnDro/Desktop/test.html'
# data_table = pd.read_html(page, attrs={"id": "emptbl"}, )
# a = 5
# "{0:0=2d}".format(a)
from django.utils.datetime_safe import date

date_time = date.today()


# print("#{0:0=3d}".format(a))
print(date_time)
