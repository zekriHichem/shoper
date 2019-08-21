from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import *
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test, login_required
from .tokens import *
from django.utils import timezone
from django.db.models import Sum,Avg
import datetime

# Create your views here.

# views autentification------------------------------------------------------------------
#login view
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse("Dashboard")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm(data=request.POST or None)

    return render(request,'registration/login.html',locals())

#signup view
def signup_page(request):
    if request.method == "POST":
        form = signupForm(request.POST or None)
        form2 = ShopeForm(request.POST or None)
        print("pass")
        print(form.is_valid())
        print(form2.is_valid())

        if form.is_valid() and form2.is_valid():
            print("hello")
            user2 = form.save()
            shope = form2.save()
            shope.logo = request.FILES.get('logo')
            shope.bill = request.FILES.get("bill")
            shope.save()
            # user2.is_staff = True
            user2.is_active = False
            user2.save()
            Shope.objects.filter(pk=shope.pk).update(user=user2)
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user2,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user2.pk)),
                'token': account_activation_token.make_token(user2),
            })
            mail_subject = 'Activate your  account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return HttpResponse('confirm your email')
        else:
            print(form2.errors)

    else:
        form = signupForm(request.POST or None)
        form2 = ShopeForm(request.POST or None)
    return render(request, 'registration/signup.html', locals())

#email confirmation view
def activate(request, uidb64, token,id):

    try:

        user = User.objects.get(pk=id)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None


    if user is not None and account_activation_token.check_token(user, token):
        return HttpResponse("votre account sera activer dans quelque instents")


    else:
        return HttpResponse('Activation link is invalid!')
# end ------------------------------------------------------------------------------------


#views shope ------------------------------------------------------------------------------
#Home view
def dashboard(request):
    user = request.user
    shope = Shope.objects.get(user=user)
    nb_selle_to_day, nb_p_b_t, money_total, product_day =  to_day_stat(shope)
    nb_product, nb_cart, cart_m = total_stat(shope)
    b_1_2,b_2_3,b_3_4 ,b_4_5 ,b_5_6 ,b_6_7 ,b_7_8 ,b_8_9 ,b_9_10 ,b_10_11,b_11_12,b_12_13,b_13_14,b_14_15,b_15_16,b_16_17,b_17_18,b_18_19,b_19_20,b_20_21,b_21_22,b_22_23,b_23_00 = hour_stat(shope)
    lun, mar, mer, jeudi, ven, sam, dim = days_stat(shope)



    return render(request,"seller/home.html",locals())

def hour_stat(shope):
    b_1_2 = Buy.objects.filter(shope=shope).filter(date__hour__in=(1,2)).aggregate(Avg("amount")).get("amount__avg")
    b_2_3 = Buy.objects.filter(shope=shope).filter(date__hour__in=(2,3)).aggregate(Avg("amount")).get("amount__avg")
    b_3_4 = Buy.objects.filter(shope=shope).filter(date__hour__in=(3,4)).aggregate(Avg("amount")).get("amount__avg")
    b_4_5 = Buy.objects.filter(shope=shope).filter(date__hour__in=(4,5)).aggregate(Avg("amount")).get("amount__avg")
    b_5_6 = Buy.objects.filter(shope=shope).filter(date__hour__in=(5,6)).aggregate(Avg("amount")).get("amount__avg")
    b_6_7 = Buy.objects.filter(shope=shope).filter(date__hour__in=(6,7)).aggregate(Avg("amount")).get("amount__avg")
    b_7_8 = Buy.objects.filter(shope=shope).filter(date__hour__in=(7,8)).aggregate(Avg("amount")).get("amount__avg")
    b_8_9 = Buy.objects.filter(shope=shope).filter(date__hour__in=(8,9)).aggregate(Avg("amount")).get("amount__avg")
    b_9_10 = Buy.objects.filter(shope=shope).filter(date__hour__in=(9,10)).aggregate(Avg("amount")).get("amount__avg")
    b_10_11 = Buy.objects.filter(shope=shope).filter(date__hour__in=(10,11)).aggregate(Avg("amount")).get("amount__avg")
    b_11_12 = Buy.objects.filter(shope=shope).filter(date__hour__in=(11,12)).aggregate(Avg("amount")).get("amount__avg")
    b_12_13 = Buy.objects.filter(shope=shope).filter(date__hour__in=(12,13)).aggregate(Avg("amount")).get("amount__avg")
    b_13_14 = Buy.objects.filter(shope=shope).filter(date__hour__in=(13,14)).aggregate(Avg("amount")).get("amount__avg")
    b_14_15 = Buy.objects.filter(shope=shope).filter(date__hour__in=(14,15)).aggregate(Avg("amount")).get("amount__avg")
    b_15_16 = Buy.objects.filter(shope=shope).filter(date__hour__in=(15,16)).aggregate(Avg("amount")).get("amount__avg")
    b_16_17 = Buy.objects.filter(shope=shope).filter(date__hour__in=(16,17)).aggregate(Avg("amount")).get("amount__avg")
    b_17_18 = Buy.objects.filter(shope=shope).filter(date__hour__in=(17,18)).aggregate(Avg("amount")).get("amount__avg")
    b_18_19 = Buy.objects.filter(shope=shope).filter(date__hour__in=(18,19)).aggregate(Avg("amount")).get("amount__avg")
    b_19_20 = Buy.objects.filter(shope=shope).filter(date__hour__in=(19,20)).aggregate(Avg("amount")).get("amount__avg")
    b_20_21 = Buy.objects.filter(shope=shope).filter(date__hour__in=(20,21)).aggregate(Avg("amount")).get("amount__avg")
    b_21_22 = Buy.objects.filter(shope=shope).filter(date__hour__in=(21,22)).aggregate(Avg("amount")).get("amount__avg")
    b_22_23 = Buy.objects.filter(shope=shope).filter(date__hour__in=(22,23)).aggregate(Avg("amount")).get("amount__avg")
    b_23_00 = Buy.objects.filter(shope=shope).filter(date__hour__in=(23,0)).aggregate(Avg("amount")).get("amount__avg")
    return b_1_2 if b_1_2 is not None else 0,b_2_3 if b_2_3 is not None else 0,\
           b_3_4 if b_3_4 is not None else 0 ,b_4_5 if b_4_5 is not None else 0\
        ,b_5_6 if b_1_2 is not None else 0,b_6_7 if b_6_7 is not None else 0\
        ,b_7_8 if b_7_8 is not None else 0,b_8_9 if b_8_9 is not None else 0 ,b_9_10 if b_9_10 is not None else 0\
        , b_10_11 if b_10_11 is not None else 0,b_11_12 if b_11_12 is not None else 0\
        ,b_12_13 if b_12_13 is not None else 0,b_13_14 if b_13_14 is not None else 0\
        ,b_14_15 if b_14_15 is not None else 0,b_15_16 if b_15_16 is not None else 0 \
        ,b_16_17 if b_16_17 is not None else 0,b_17_18 if b_17_18 is not None else 0\
        ,b_18_19 if b_18_19 is not None else 0,b_19_20 if b_19_20 is not None else 0\
        ,b_20_21 if b_20_21 is not None else 0,b_21_22 if b_21_22 is not None else 0\
        ,b_22_23 if b_22_23 is not None else 0,b_23_00 if b_23_00 is not None else 0

def days_stat(shope):
    lun = Buy.objects.filter(shope=shope).filter(date__week_day=0).aggregate(Avg("amount")).get("amount__avg")
    mar = Buy.objects.filter(shope=shope).filter(date__week_day=1).aggregate(Avg("amount")).get("amount__avg")
    mer = Buy.objects.filter(shope=shope).filter(date__week_day=2).aggregate(Avg("amount")).get("amount__avg")
    jeudi = Buy.objects.filter(shope=shope).filter(date__week_day=3).aggregate(Avg("amount")).get("amount__avg")
    ven = Buy.objects.filter(shope=shope).filter(date__week_day=4).aggregate(Avg("amount")).get("amount__avg")
    sam = Buy.objects.filter(shope=shope).filter(date__week_day=5).aggregate(Avg("amount")).get("amount__avg")
    dim = Buy.objects.filter(shope=shope).filter(date__week_day=6).aggregate(Avg("amount")).get("amount__avg")
    return lun if lun is not None else 0,mar if mar is not None else 0,mer if mer is not None else 0,jeudi if jeudi is not None else 0\
        ,ven if ven is not None else 0,sam if sam is not None else 0,dim if dim is not None else 0




def total_stat(shope):
    nb_product = Product.objects.filter(shope=shope).count()
    nb_cart = Cart.objects.filter(shope=shope).count()
    cart_m = Cart.objects.filter(shope=shope).filter(date__month=timezone.now().date().month).aggregate(Sum("total")).get("total__sum")
    return nb_product,nb_cart,cart_m if cart_m is not None else 0


def to_day_stat(shope):
    nb_selle_to_day = Cart.objects.filter(shope=shope).filter(date__date=timezone.now().date()).count()
    carts = Cart.objects.filter(shope=shope).filter(date__date=timezone.now().date())
    nb_p_b_t = 0
    money_total = 0
    products = []
    amounts = []
    for cart in carts:
        money_total += cart.total
        for buy in cart.buys.all():
            if products.__contains__(buy.product):
                pass
            else:
                products.append(buy.product)
            nb_p_b_t += buy.amount
    for product in products:
        result = Buy.objects.filter(shope=shope).filter(date__date=timezone.now().date()).filter(
            product=product).aggregate(Sum("amount"))
        amounts.append(result)
    amount_i = -1
    amount_val = 0
    i = 0
    for amount in amounts:
        if amount_i == -1:
            amount_i = i
            amount_val = amount.get("amount__sum")
        if amount.get("amount__sum") > amount_val:
            amount_i = i
            amount_val = amount.get("amount__sum")

        i += 1
    if amount_i == -1 :
        product_day = None
    else:
        product_day = products[amount_i]


    return nb_selle_to_day,nb_p_b_t,money_total,product_day


#Show product view
@login_required()
def products(request):
    user = request.user
    shope = Shope.objects.get(user=user)
    products = Product.objects.filter(shope=shope)
    return render(request,"seller/product.html",locals())

#Single product view
@login_required()
def signleProduct(request,id):
    user = request.user
    shope = Shope.objects.get(user=user)
    product = Product.objects.get(id=id)
    buys = Buy.objects.filter(product=product).count()
    if request.method == "POST":
        product.title = request.POST["title"]
        product.idd = request.POST["idd"]
        product.discription = request.POST["discription"]
        product.price = request.POST["price"]
        product.price_buy = request.POST["pricebuy"]
        product.nb = request.POST["amount"]
        product.add_field = request.POST["addition"]
        product.price_reduction = request.POST["pricer"]


        if request.FILES.get('image') is None:
            pass
        else:
            product.first_images = request.FILES.get('image')
        product.save()
        edited = True
        return render(request, "seller/singleproduct.html", locals())
    else:
        return render(request, "seller/singleproduct.html", locals())

    return render(request,"seller/singleproduct.html",locals())
#Add product view
@login_required()
def addProduct(request):
    user = request.user
    shope = Shope.objects.get(user = user)
    if request.method == "POST" :
        title = request.POST["title"]
        idd = request.POST["idd"]
        discription = request.POST["discription"]
        price = request.POST["price"]
        price_buy = request.POST["pricebuy"]
        nb = request.POST["amount"]
        add_field = request.POST["addition"]
        first_image = request.FILES.get("image")
        price_reduction = 0
        Product.objects.create(shope=shope,title=title,idd=idd,discription=discription,price=price,price_buy=price_buy
                               ,nb=nb,add_field=add_field,first_images=first_image,price_reduction=price_reduction)
        return render(request, "seller/add.html",{"is_added":True},locals())


    else:
        return render(request, "seller/add.html",locals())

    return render(request,"seller/add.html",locals())

@login_required()
def sup_product(request,id):
    user = request.user
    shope = Shope.objects.get(user=user)
    Product.objects.get(id=id).delete()
    return redirect("products")


buys = []

def recive_buy(request):
    user = request.user
    shope = Shope.objects.get(user=user)
    if request.method == "GET":
        idp = request.GET.get("idp")
        qtt = request.GET.get("qtt")
        product = Product.objects.get(id=idp)
        buy=Buy.objects.create(shope=shope,product=product,amount=qtt,date=timezone.now())
        buys.append(buy.id)
        return  JsonResponse({"id":buy.id})
    return JsonResponse({"error":"ok"})

def recive_cart(request):
    buys_obj = []
    user = request.user
    shope = Shope.objects.get(user=user)
    print(buys)
    cart = Cart.objects.create(shope=shope,date=timezone.now())
    total = 0
    for buy in buys:
        b=Buy.objects.get(id=buy)
        cart.buys.add(b)
        total += b.product.price * b.amount
    cart.total=total
    cart.save()
    buys.clear()

    return JsonResponse({'error':'ok'})




#Buy view
@login_required()
def buy(request):
    user = request.user
    shope = Shope.objects.get(user = user)
    products = Product.objects.filter(shope=shope)
    carts = Cart.objects.filter(shope=shope).order_by("date").reverse()
    return render(request,"seller/buy.html",locals())








# end ---------------------------------------------------------------------------------------------------------------------

# setting views -----------------------------------------------------------------------------------------------------------



