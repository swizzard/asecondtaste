from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class MenuItem(models.Model):
    ##property stuff via http://stackoverflow.com/questions/1454727/do-properties-work-on-django-model-fields
    def format_price(self, price):
        formatted_price = "${0:0<4,.2f}".format(float(price))
        return formatted_price

    @property
    def formatted_price(self):
        if self.__formatted_price:
            return self.__formatted_price
        else:
            return self.price

    @formatted_price.setter
    def formatted_price(self):
        try:
            self.__formatted_price = self.format_price(self.__formatted_price)
        except ValueError:
            self.__formatted_price = self.price

    dish=models.OneToOneField('Dish',to_field='mk', null=True, blank=True)
    price=models.CharField(max_length=10,blank=True, null=True)
#   course=models.CharField(max_length=100,unique=False)
    page=models.ForeignKey('MenuPage',to_field='mk', null=True, blank=True)
    mk=models.CharField(max_length=100,unique=True)
    __formatted_price = models.CharField(max_length=12,blank=True,null=True,db_column='formatted_price',default="")

    def __unicode__(self):
        try:
            return self.dish__name
        except ObjectDoesNotExist:
            pass

class Menu(models.Model):
#     def to_period(self, year):#adapted from http://stackoverflow.com/questions/2272149/round-to-5or-other-number-in-python
#         try:
#             p=int(10*round(float(int(year))/10))
#             if p < self.year:
#                 return "%s-%s"%(p,p+5)
#             else:
#                 return "%s-%s"%(p-5,p)
#         except (ValueError,TypeError):
#             return ""
#
#     @property
#     def period(self):
#         if self.__period:
#             return self.__period
#         else:
#             return self.year
#
#     @period.setter
#     def period(self):
#         self.__period = self.to_period(self.year)
#     def __unicode__(self):
#         if self.restaurant:
#             return self.restaurant
#         else:
#             return self.mk
    restaurant=models.TextField(unique=False,blank=True,null=True)
    year=models.CharField(max_length=4,unique=False,blank=True,null=True)
    location=models.TextField(unique=False,blank=True,null=True)
    status=models.CharField(unique=False,max_length=20)
    mk=models.CharField(max_length=100,unique=True)
#     __period=models.CharField(max_length=9,unique=False, blank=True, null=True, db_column="period",default="")
    language = models.CharField(unique=False,max_length=30)

class MenuPage(models.Model):
    mk=models.CharField(max_length=100,unique=True)
    menu=models.ForeignKey("Menu",to_field='mk', null=True, blank=True)

class Dish(models.Model):
    def __unicode__(self):
        return self.name

    full_name = models.TextField(unique=False)
    name=models.CharField(unique=False, max_length=255)
    mk=models.CharField(max_length=100,unique=True)
    classification=models.ForeignKey('Classification', null=True, blank=True)
    class Meta:
        verbose_name_plural = "Dishes"

class Classification(models.Model):
    def __unicode__(self):
        if self.classification:
            return self.classification
        else:
            return "none"
    dessert = "Dessert"
    main_ = "Main"
    appetizer = "Appetizer"
    none_ = "None"
    classification_choices = (
        (dessert, "Dessert"),
        (main_, "Main"),
        (appetizer, "Appetizer"),
        (none_, "Unclassified"),
        )
    classification=models.CharField(unique=False,max_length=9,choices=classification_choices)
