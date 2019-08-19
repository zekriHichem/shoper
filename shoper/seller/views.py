from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test
from .tokens import *

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
    return render(request,"seller/home.html")

#Show product view
def products(request):
    return render(request,"seller/product.html")

#Single product view
def signleProduct(request):
    return render(request,"seller/singleproduct.html")
#Add product view
def addProduct(request):
    return render(request,"seller/add.html")

#Buy view
def buy(request):
    return render(request,"seller/buy.html")


# end ---------------------------------------------------------------------------------------------------------------------

# setting views -----------------------------------------------------------------------------------------------------------



