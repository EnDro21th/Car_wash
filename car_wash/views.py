import datetime
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.datetime_safe import date

from .form import *
from django.contrib.auth.models import User
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, content_dict={}):
    template = get_template(template_src)
    html = template.render(content_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    # pdf = pisa.(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def m(request):
    restock_count = Stock.objects.all().filter(reorder__gte=F('qty')).exclude(catid='4').count()
    restock = Stock.objects.all().filter(reorder__gte=F('qty')).exclude(catid='4')
    stocklist = Stock.objects.all().filter(reorder__lt=F('qty')).exclude(catid='4')
    stockall = Stock.objects.exclude(catid='4')
    customerlist = Customer.objects.all()
    Import_form = ImportForm()
    Importdetail_form = ImportdetailForm()
    Stock_form = StockForm()
    Category_form = CategoryForm()
    cartype = Stock.objects.filter(catid='4')
    oiltype = Stock.objects.filter(catid='2')
    drinktype = Stock.objects.filter(catid='1')
    acctype = Stock.objects.filter(catid='3')
    expensetype = Expensetype.objects.all()

    sid_count = Sell.objects.filter(status='Hold').count()
    sid_count1 = Sell.objects.filter(status='Hold')[:1]
    sid_count2 = Sell.objects.filter(status='Hold')[1:2]
    sid_count3 = Sell.objects.filter(status='Hold')[2:3]
    sid_count4 = Sell.objects.filter(status='Hold')[3:4]
    sid_count5 = Sell.objects.filter(status='Hold')[4:5]
    sid_count6 = Sell.objects.filter(status='Hold')[5:6]
    sid_count7 = Sell.objects.filter(status='Hold')[6:7]
    sid_count8 = Sell.objects.filter(status='Hold')[7:8]
    sid_count9 = Sell.objects.filter(status='Hold')[8:9]
    sid_count10 = Sell.objects.filter(status='Hold')[9:10]
    sid_count11 = Sell.objects.filter(status='Hold')[10:11]
    sid_count12 = Sell.objects.filter(status='Hold')[11:12]
    sid_count13 = Sell.objects.filter(status='Hold')[12:13]
    sid_count14 = Sell.objects.filter(status='Hold')[13:14]
    sid_count15 = Sell.objects.filter(status='Hold')[14:15]
    sid_count16 = Sell.objects.filter(status='Hold')[15:16]
    sid_count17 = Sell.objects.filter(status='Hold')[16:17]
    sid_count18 = Sell.objects.filter(status='Hold')[17:18]
    sid_count19 = Sell.objects.filter(status='Hold')[18:19]
    sid_count20 = Sell.objects.filter(status='Hold')[19:20]
    sid_count21 = Sell.objects.filter(status='Hold')[20:21]
    sid_count22 = Sell.objects.filter(status='Hold')[21:22]
    sid_count23 = Sell.objects.filter(status='Hold')[22:23]
    sid_count24 = Sell.objects.filter(status='Hold')[23:24]
    sid_count25 = Sell.objects.filter(status='Hold')[24:25]
    sid_count26 = Sell.objects.filter(status='Hold')[25:26]
    sid_count27 = Sell.objects.filter(status='Hold')[26:27]
    sid_count28 = Sell.objects.filter(status='Hold')[27:28]
    sid_count29 = Sell.objects.filter(status='Hold')[28:29]
    sid_count30 = Sell.objects.filter(status='Hold')[29:30]
    sid_count31 = Sell.objects.filter(status='Hold')[30:31]
    sid_count32 = Sell.objects.filter(status='Hold')[31:32]
    sid_count33 = Sell.objects.filter(status='Hold')[32:33]
    sid_count34 = Sell.objects.filter(status='Hold')[33:34]
    sid_count35 = Sell.objects.filter(status='Hold')[34:35]
    sid_count36 = Sell.objects.filter(status='Hold')[35:36]

    stockdict = {'stock': stocklist, 'cus': customerlist, 'Import_form': Import_form, 'restock': restock,
                 'Importdetail_form': Importdetail_form, 'Stock_form': Stock_form,
                 'stockall': stockall, 'cartype': cartype, 'Category_form': Category_form,
                 'expensetype': expensetype, 'oiltype': oiltype, 'drinktype': drinktype, 'acctype': acctype,
                 'sid_count': "{0:0=3d}".format(sid_count), 'sid_count1': sid_count1, 'sid_count2': sid_count2,
                 'sid_count3': sid_count3, 'restock_count': "{0:0=3d}".format(restock_count),
                 'sid_count4': sid_count4, 'sid_count5': sid_count5, 'sid_count6': sid_count6,
                 'sid_count7': sid_count7, 'sid_count8': sid_count8, 'sid_count9': sid_count9,
                 'sid_count10': sid_count10, 'sid_count12': sid_count12, 'sid_count13': sid_count13,
                 'sid_count14': sid_count14, 'sid_count15': sid_count15, 'sid_count16': sid_count16,
                 'sid_count17': sid_count17, 'sid_count18': sid_count18, 'sid_count19': sid_count19,
                 'sid_count20': sid_count20, 'sid_count21': sid_count21, 'sid_count23': sid_count23,
                 'sid_count24': sid_count24, 'sid_count25': sid_count25, 'sid_count26': sid_count26,
                 'sid_count27': sid_count27, 'sid_count28': sid_count28, 'sid_count29': sid_count29,
                 'sid_count30': sid_count30, 'sid_count31': sid_count31, 'sid_count32': sid_count32,
                 'sid_count33': sid_count33, 'sid_count34': sid_count34, 'sid_count35': sid_count35,
                 'sid_count36': sid_count36, 'sid_count22': sid_count22, 'sid_count11': sid_count11}
    return render(request, 'page1.html', context=stockdict)


def login_page(request):
    if request.method == 'POST':
        user = request.POST.get('Editbox1')
        password = request.POST.get('Editbox2')
        log = authenticate(request, username=user, password=password)
        if log is not None:
            login(request, log)
            return redirect(m)
        else:
            messages.info(request, '*Incorrect Username or Password')
    context = {}
    return render(request, 'index.html', context)


def create_Import(request):
    date = datetime.datetime.now()
    sid = request.user.id
    user = User.objects.get(id=sid)
    discount_total = request.POST.get('txtbox_totaldis')
    discount_total_str = discount_total[19:]
    grand_total = request.POST.get('txtbox_totalimport')
    grand_total_str = grand_total[10:]
    supplyid = request.POST.get('combobox_supplier')
    suppid = Supplier.objects.get(suppid=supplyid)
    Import_form = Import(date=date, discount_total=discount_total_str, grand_total=grand_total_str, suppid=suppid,
                         sid=user)
    Import_form.save()
    importid = Import.objects.latest('importid')
    loop = request.POST.get('data_post')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_' + str(i))
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)
        urm = request.POST.get('urm_' + str(i))
        urm_spit = urm.split(' x ')
        for a in urm_spit:
            urm = a[1]
        qty = request.POST.get('qty_' + str(i))
        cost = request.POST.get('cost_' + str(i))
        dis = request.POST.get('dis_' + str(i))
        amount = request.POST.get('amount_' + str(i))
        i += 1
        Importdetail_form = Importdetail(importid=importid, productid=pname, qty=qty, cost=cost, discount=dis,
                                         total=amount, description=urm)
        Importdetail_form.save()

        Stock_form = Stock.objects.get(productid=item)
        Stock_form.qty = F('qty') + int(qty)
        avg_cost = ((int(qty) * (float(cost) / float(a))) + (F('qty') * F('cost'))) / (int(qty) + F('qty'))
        Stock_form.cost = avg_cost
        Stock_form.save()

    return redirect('/main')


def create_ajustment(request):
    date = request.POST.get('datepicker_adjustment')
    sid = request.user.id
    user = User.objects.get(id=sid)
    grand_total = request.POST.get('txtbox_total_adjustment')
    grand_total_str = grand_total[2:]
    appby = request.POST.get('combobox_approvedby')
    ajustment_form = Ajustment(date=date, sid=user, total=grand_total_str, appby=appby)
    ajustment_form.save()

    ajustmentid = Ajustment.objects.latest('ajid')
    loop = request.POST.get('data_post_ajm')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_adj_' + str(i))
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)
        qty = request.POST.get('qty_adj_' + str(i))
        des = request.POST.get('des_adj_' + str(i))
        price = request.POST.get('price_adj_' + str(i))
        i += 1
        ajustmentdetail_form = Ajustmentdetal(ajid=ajustmentid, productid=pname, description=des, qty=qty,
                                              brokenprice=price)
        ajustmentdetail_form.save()

        Stock_form = Stock.objects.get(productid=item)
        Stock_form.qty = F('qty') - int(qty)
        Stock_form.save()

    return redirect('/main')


def create_expense(request):
    date = datetime.datetime.now()
    sid = request.user.id
    user = User.objects.get(id=sid)
    grand_total = request.POST.get('txtbox_totalexpense')
    grand_total_str = grand_total[9:]
    appby = request.POST.get('combobox_approvedbyexpense')
    expense_form = Expense(sid=user, date=date, total=grand_total_str, appby=appby)
    expense_form.save()

    exid = Expense.objects.latest('exid')
    loop = request.POST.get('data_post_exp')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('extype_' + str(i))
        extyid = Expensetype.objects.filter(extypename=name).values_list('pk', flat=True)
        for item in extyid:
            pname = Expensetype.objects.get(extypeid=item)
        qty = request.POST.get('qty_exp_' + str(i))
        des = request.POST.get('des_exp_' + str(i))
        price = request.POST.get('price_exp_' + str(i))
        i += 1
        expensedetail_form = Expensedetail(exid=exid, extypeid=pname, desciption=des, cost=price, qty=qty)
        expensedetail_form.save()

    return redirect('/main')


def recipt(request):
    try:
        date = datetime.datetime.now()
        sid = request.user.id
        user = User.objects.get(id=sid)
        sellid = request.POST.get('txtsellid')
        selldetail = Selldetail.objects.filter(sellid=sellid)
        total = request.POST.get('total_txt')
        after_vat_total = float(total[:-5]) * 0.1
        all_total = float(total[:-5]) + float(after_vat_total)
        recieve_d = request.POST.get('txtbox_InputUSD')
        recieve_r = request.POST.get('txtbox_InputRiel')
        change_d = request.POST.get('change_usd_txt')
        change_r = request.POST.get('change_riel_txt')
        dis = request.POST.get('discount_txt')
        name = request.POST.get('txtbox_billto')
        cid = Customer.objects.get(cphonenumber=name)

        sell_form = Sell(sellid=sellid, date=date, sid=user, cid=cid, vat=after_vat_total, discount_total=dis[:-5],
                         grant_total=all_total, status='Done')
        sell_form.save()

        catpro = Stock.objects.all().exclude(catid__in=[2, 4])
        service_pro = Selldetail.objects.filter(sellid=sellid).filter(productid__in=catpro)

        for items in service_pro:
            name = items.productid
            qty = items.qty

            Stock_form = Stock.objects.get(productname=name)
            Stock_form.qty = F('qty') - int(qty)
            Stock_form.save()

        dict = {'date': date, 'user': user, 'sellid': sellid, 'selldetail': selldetail, 'total': total[:-5],
                'after_vat_total': round(after_vat_total, 2), 'all_total': round(all_total, 2), 'recieve_d': recieve_d,
                'recieve_r': recieve_r, 'change_d': change_d, 'change_r': change_r}
        # return render(request, 'recipt.html', context=dict)
        template = get_template('recipt.html')
        html = template.render(dict)

        file = open('recipt.pdf', "w+b")
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

        file.seek(0)
        pdf = file.read()
        file.close()
        return HttpResponse(pdf, content_type='application/pdf;')

    except:
        return redirect('/main')


def print(request):
    date = datetime.datetime.now()
    sid = request.user.id
    user = User.objects.get(id=sid)
    sellid = request.POST.get('txtsellid')
    selldetail = Selldetail.objects.filter(sellid=sellid)
    total = request.POST.get('subtotal_txt')
    after_vat_total = float(total[:-5]) * 0.1
    all_total = float(total[:-5]) + float(after_vat_total)

    dict = {'date': date, 'user': user, 'sellid': sellid, 'selldetail': selldetail, 'total': total[:-5],
            'after_vat_total': round(after_vat_total, 2), 'all_total': all_total}

    template = get_template('print.html')
    html = template.render(dict)

    file = open('print.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, content_type='application/pdf;')


def report_today(request):
    date_start = date.today()
    date_end = date.today()
    date_day = date.today().day
    date_month = date.today().month
    date_year = date.today().year
    sid = request.user.id
    user = User.objects.get(id=sid)
    serviceid = Sell.objects.filter(date__day=date_day, date__month=date_month, date__year=date_year)
    total_service = 0
    if serviceid:
        for items in serviceid:
            total_service += float(items.grant_total)
    else:
        total_service = 0

    expenseid = Expense.objects.filter(date__day=date_day, date__month=date_month, date__year=date_year)
    total_expense = 0
    if expenseid:
        for item in expenseid:
            total_expense += float(item.total)
    else:
        total_expense = 0

    ajustid = Ajustment.objects.filter(date__day=date_day, date__month=date_month, date__year=date_year)
    total_aj = 0
    if ajustid:
        for itemx in ajustid:
            total_aj += float(itemx.total)
    else:
        total_aj = 0

    ex_to = float(total_aj) + float(total_expense)
    g_t = float(total_service) - float(ex_to)

    dict = {'user': user, 'date_start': date_start, 'date_end': date_end, 'total_service': round(total_service, 2),
            'serviceid': serviceid,
            'total_expense': round(total_expense, 2), 'expenseid': expenseid, 'total_aj': round(total_aj, 2), 'ajustid': ajustid,
            'ex_to': round(ex_to, 2), 'g_t': round(g_t, 2)}
    return render(request, 'Report.html', context=dict)


def report_date(request):
    date_start = request.POST.get('datepicker_from')
    date_end = request.POST.get('datepicker_to')
    sid = request.user.id
    user = User.objects.get(id=sid)
    serviceid = Sell.objects.filter(date__range=(date_start, date_end))
    total_service = 0
    if serviceid:
        for items in serviceid:
            total_service += float(items.grant_total)
    else:
        total_service = 0

    expenseid = Expense.objects.filter(date__range=[date_start, date_end])
    total_expense = 0
    if expenseid:
        for item in expenseid:
            total_expense += float(item.total)
    else:
        total_expense = 0

    ajustid = Ajustment.objects.filter(date__range=[date_start, date_end])
    total_aj = 0
    if ajustid:
        for itemx in ajustid:
            total_aj += float(itemx.total)
    else:
        total_aj = 0

    ex_to = float(total_aj) + float(total_expense)
    g_t = float(total_service) - float(ex_to)

    dict = {'user': user, 'date_start': date_start, 'date_end': date_end, 'total_service': round(total_service),
            'serviceid': serviceid,
            'total_expense': round(total_expense, 2), 'expenseid': expenseid, 'total_aj': round(total_aj, 2), 'ajustid': ajustid,
            'ex_to': round(ex_to, 2), 'g_t': round(g_t, 2)}
    return render(request, 'Report.html', context=dict)


def create_service(request):
    date = datetime.datetime.now()
    sid = request.user.id
    user = User.objects.get(id=sid)
    num = request.POST.get('txtbox_phonenumber_payment')
    try:
        cid = Customer.objects.get(cphonenumber=num)
        cust_form = Customer.objects.get(cphonenumber=cid)
        cust_form.count = F('count') + 1
        cust_form.total_count = F('total_count') + 1
        cid.lastdate = date
        cust_form.save()
    except Customer.DoesNotExist:
        cid = Customer(cphonenumber=num)
        cid.save()
        cid.lastdate = date
        cid.save()
    service_form = Sell(date=date, cid=cid, sid=user, vat='0', discount_total='0', grant_total='0', status='Hold')
    service_form.save()
    sellid = Sell.objects.latest('sellid')

    loop = request.POST.get('data_post_ser')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_service_' + str(i))
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)
        qty = request.POST.get('qty_service_' + str(i))
        price = request.POST.get('cost_service_' + str(i))
        total = int(qty) * float(price)
        i += 1
        servicedetail_form = Selldetail(sellid=sellid, productid=pname, qty=qty, price=price, discount='0', total=total)
        servicedetail_form.save()

    return redirect('/main')


def more_service(request):
    name = request.POST.get('txtbox_displayphonenumber')
    cid = Customer.objects.get(cphonenumber=name)
    sellid = request.POST.get('customerID')
    selldetail = Selldetail.objects.all().filter(sellid=sellid[10:])
    cartype = Stock.objects.filter(catid='4')
    oiltype = Stock.objects.filter(catid='2')
    drinktype = Stock.objects.filter(catid='1')
    acctype = Stock.objects.filter(catid='3')
    stockdict = {'cartype': cartype, 'oiltype': oiltype, 'drinktype': drinktype, 'acctype': acctype,
                 'cid': cid, 'selldetail': selldetail, 'sellid': sellid[10:]}
    return render(request, 'More_Service.html', context=stockdict)


def save_service(request):
    sellid = request.POST.get('sellid')
    sell = Sell.objects.filter(sellid=sellid).values_list('pk', flat=True)
    for i in sell:
        sell_id = Sell.objects.get(sellid=i)
    delete_sellid = Selldetail.objects.filter(sellid=sellid).delete()
    loop = request.POST.get('data_post_ser')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_service_' + str(i))
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)

        qty = request.POST.get('qty_service_' + str(i))
        price = request.POST.get('cost_service_' + str(i))
        if qty == 'None':
            break
        i += 1
        total = int(qty) * float(price)

        servicedetail_form = Selldetail(sellid=sell_id, productid=pname, qty=qty, price=price, discount='0',
                                        total=total)
        servicedetail_form.save()

    return redirect('/main')


def checkout(request):
    name = request.POST.get('txtbox_displayphonenumber')
    cid = Customer.objects.get(cphonenumber=name)
    sellid = request.POST.get('customerID')
    selldetail = Selldetail.objects.filter(sellid=sellid[10:])
    total = 0
    try:
        for item in selldetail:
            total += item.total
        date = datetime.datetime.now()
        limit = Customer.objects.all().filter(cphonenumber=name).values_list('limit', flat=True)
        for itemx in limit:
            l = itemx
        count = Customer.objects.all().filter(cphonenumber=name).values_list('count', flat=True)
        for item in count:
            c = item
        cat4 = Stock.objects.all().filter(catid=4)
        service = Selldetail.objects.filter(sellid=sellid[10:]).filter(productid__in=cat4).values_list('total',
                                                                                                       flat=True)
        mod = int(c) // (int(l) - 1)
        if mod > 0:
            minn = min(service)
            vat = round((float(total) * 0.1), 2)
            all_total = float(total) + float(vat) - minn
            cust_form = Customer.objects.get(cphonenumber=cid)
            cust_form.count = F('count') - (F('limit') - 1)
            cust_form.save()

            stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid[10:], 'date': date,
                         'total': total,
                         'min': minn,
                         'all_total': all_total, 'vat': vat}
        if mod == 0:
            vat = round((float(total) * 0.1), 2)
            all_total = float(total) + float(vat)
            stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid[10:], 'date': date,
                         'total': total,
                         'all_total': all_total, 'min': 0, 'vat': vat}
        return render(request, 'Checkout.html', context=stockdict)

    except:
        return redirect('/main')


def checkout_moreservice(request):
    name = request.POST.get('txtbox_phonenumber_payment')
    date = datetime.datetime.now()
    cid = Customer.objects.get(cphonenumber=name)
    sellid = request.POST.get('sellid')
    sell = Sell.objects.filter(sellid=sellid).values_list('pk', flat=True)
    for i in sell:
        sell_id = Sell.objects.get(sellid=i)
    delete_sellid = Selldetail.objects.filter(sellid=sellid).delete()
    loop = request.POST.get('data_post_ser')
    i = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_service_' + str(i))
        if name == 'None':
            break
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)
        qty = request.POST.get('qty_service_' + str(i))
        price = request.POST.get('cost_service_' + str(i))
        i += 1
        total = int(qty) * float(price)
        servicedetail_form = Selldetail(sellid=sell_id, productid=pname, qty=qty, price=price, discount='0',
                                        total=total)
        servicedetail_form.save()

    selldetail = Selldetail.objects.filter(sellid=sellid)
    total = 0
    for item in selldetail:
        total += item.total
    limit = Customer.objects.all().filter(cphonenumber=cid).values_list('limit', flat=True)
    for itemx in limit:
        l = itemx
    count = Customer.objects.all().filter(cphonenumber=cid).values_list('count', flat=True)
    for item in count:
        c = item
    cat4 = Stock.objects.all().filter(catid=4)
    service = Selldetail.objects.filter(sellid=sellid).filter(productid__in=cat4).values_list('total',
                                                                                              flat=True)
    mod = int(c) // (int(l) - 1)
    if mod > 0:
        minn = min(service)
        vat = round((float(total) * 0.1), 2)
        all_total = float(total) + float(vat) - minn
        cust_form = Customer.objects.get(cphonenumber=cid)
        cust_form.count = F('count') - (F('limit') - 1)
        cust_form.save()
        stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid, 'date': date,
                     'total': total,
                     'min': minn,
                     'all_total': all_total, 'vat': vat}
    if mod == 0:
        vat = round((float(total) * 0.1), 2)
        all_total = float(total) + float(vat)
        stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid, 'date': date,
                     'total': total,
                     'all_total': all_total, 'min': 0, 'vat': vat}
    return render(request, 'Checkout.html', context=stockdict)


def checkout_new(request):
    date = datetime.datetime.now()
    sid = request.user.id
    user = User.objects.get(id=sid)
    num = request.POST.get('txtbox_phonenumber_payment')
    try:
        cid = Customer.objects.get(cphonenumber=num)
        cust_form = Customer.objects.get(cphonenumber=cid)
        cust_form.count = F('count') + 1
        cust_form.total_count = F('total_count') + 1
        cid.lastdate = date
        cust_form.save()
    except Customer.DoesNotExist:
        cid = Customer(cphonenumber=num)
        cid.save()
        cid.lastdate = date
        cid.save()
    service_form = Sell(date=date, cid=cid, sid=user, vat='0', discount_total='0', grant_total='0', status='Hold')
    service_form.save()
    sellid = Sell.objects.latest('sellid')

    loop = request.POST.get('data_post_ser')
    i = 0
    total = 0
    while i <= int(loop) - 1:
        name = request.POST.get('pname_service_' + str(i))
        productid = Stock.objects.filter(productname=name).values_list('pk', flat=True)
        for item in productid:
            pname = Stock.objects.get(productid=item)
        qty = request.POST.get('qty_service_' + str(i))
        price = request.POST.get('cost_service_' + str(i))
        total = int(qty) * float(price)
        i += 1
        servicedetail_form = Selldetail(sellid=sellid, productid=pname, qty=qty, price=price, discount='0', total=total)
        servicedetail_form.save()

    selldetail = Selldetail.objects.filter(sellid=sellid)
    total = 0
    for item in selldetail:
        total += item.total
    limit = Customer.objects.all().filter(cphonenumber=cid).values_list('limit', flat=True)
    for itemx in limit:
        l = itemx
    count = Customer.objects.all().filter(cphonenumber=cid).values_list('count', flat=True)
    for item in count:
        c = item
    cat4 = Stock.objects.all().filter(catid=4)
    service = Selldetail.objects.filter(sellid=sellid).filter(productid__in=cat4).values_list('total',
                                                                                              flat=True)
    mod = int(c) // int(l)
    if mod > 0:
        minn = min(service)
        vat = round((float(total) * 0.1), 2)
        all_total = float(total) + float(vat) - minn
        cust_form = Customer.objects.get(cphonenumber=cid)
        cust_form.count = F('count') - (F('limit') - 1)
        cust_form.save()

        stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid, 'date': date,
                     'total': total,
                     'min': minn,
                     'all_total': all_total, 'vat': vat}
    if mod == 0:
        vat = round((float(total) * 0.1), 2)
        all_total = float(total) + float(vat)
        stockdict = {'cid': cid, 'selldetail': selldetail, 'sellid': sellid, 'date': date,
                     'total': total,
                     'all_total': all_total, 'min': 0, 'vat': vat}
    return render(request, 'Checkout.html', context=stockdict)
