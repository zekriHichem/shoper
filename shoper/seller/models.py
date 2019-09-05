from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
TYPE_SHOPE = (("MC","men clothing"),("WC","women clothes"),("IN","Informatique"),("FU","furniture",),("CO","cosmetic"))
WILLAYA = (("1","Adrar"),("2","Chelf"),("3","Laghouat"),("4","Oum El Bouaghi"),("5","Batna"),("6","Béjaïa"),("7","Biskra"),
           ("8","Béchar"),("9","Blida"),("10","Bouira"),("11","Tamanrasset"),("12","Tébessa"),("13","Tlemcen"),("14","Tiaret"),
           ("15","Tizi Ouzou"),("16","Alger"),("17","Djelfa"),("18","Jijel"),("19","Sétif"),("20","Saïda"),("21","Skikda"),
           ("22","Sidi Bel Abbès",),("23","Annaba",), ("24","Guelma", ),("25","Constantine",),("26","Médéa",),("27","Mostaganem",),
           ("28","M'Sila",) ,("29","Mascara",),("30","Ouargla",),("31","Oran",),("32","El Bayadh",),("33","Illizi",),
           ("34","Bordj Bou Arreridj",),("35","Boumerdès",),("36","El Tarf",),("37","Tindouf",), ("38","Tissemsilt", ),
           ("39","El Oued",),("40","Khenchela",),("41","Souk Ahras",),("42","Tipaza",), ("43","Mila",),
           ("44","Aïn Defla",),("45","Naâma",),("46","Aïn Témouchent",),("47","Ghardaïa",),("48","Relizane",))
FUNCTIONS = (("1","provider"),("2","Doctor"),("3","police"),("4","firefighter"),("5","staff"))
class Shope(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,unique=True,null=True)
    date_creation = models.DateTimeField(null=True,blank=True)
    type_shope = models.CharField(choices=TYPE_SHOPE,max_length=50)
    num_phone = models.CharField(max_length=15)
    wilaya = models.CharField(choices=WILLAYA,max_length=255)
    address = models.CharField(max_length=255)
    logo = models.FileField(upload_to='logo', default="logo/default.png", verbose_name="")
    bill = models.FileField(upload_to='bill', default="logo/default.png")

class Product(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    idd = models.CharField(max_length=50)
    discription = models.TextField()
    price_buy= models.FloatField()
    price = models.FloatField()
    price_reduction = models.FloatField()
    nb = models.IntegerField()
    first_images = models.FileField(upload_to='image', default="logo/default.png", verbose_name="")
    add_field = models.TextField()
    is_in_reduction =models.BooleanField(default=False)

    @property
    def get_price(self):
        if self.is_in_reduction :
            return self.price_reduction
        else:
            return self.price

class Buy(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField()
    @property
    def total (self):
        if self.product.is_in_reduction :
            return self.product.price_reduction * self.amount
        else:
            return self.product.price * self.amount

class Cart (models.Model) :
    shope = models.ForeignKey(Shope,on_delete=models.CASCADE)
    buys = models.ManyToManyField(Buy,null = True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)

class Contact(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField(null=True,blank=True)
   # func = models.CharField(max_length=50,choices=FUNCTIONS)
