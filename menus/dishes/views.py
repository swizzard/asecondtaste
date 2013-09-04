# Create your views here.
from django.shortcuts import render_to_response, render
from models import MenuItem, Menu, Dish, Classification, MenuPage
from dishes.forms import SearchForm
from django.forms.formsets import formset_factory, BaseFormSet
import re
from django.db.models import Q
from django.views.generic.base import View
from django.core.exceptions import ValidationError
import operator


class Search(View):
    def __init__(self):
        self.formset = formset_factory(SearchForm, extra=5)

    def var_reduce(self, op, slice):
        if op == "and":
            return reduce(operator.and_,slice)
        elif op == "or":
            return reduce(operator.or_,slice)

    def get_fk(self, parameter, query, neg=False):
        filter_keys = {
                        "dish-name":Q(dish__name__icontains=query),
                        "regex":Q(dish__full_name__regex=r'{0}'.format(re.escape(query))),
                        "course":Q(dish__classification__classification__iexact=query),
                        "year":Q(page__menu__year__exact=query),
                        "period":Q(page__menu__year__range=query.split('-')),
                        "location":Q(page__menu__location__icontains=query),
                        "restaurant":Q(page__menu__restaurant__icontains=query)
                        }
        neg_filter_keys = {
                        "dish-name": ~Q(dish__name__icontains=query),
                        "regex": ~Q(dish__full_name__regex=r'{0}'.format(re.escape(query))),
                        "course": ~Q(dish__classification__classification__iexact=query),
                        "year": ~Q(page__menu__year__exact=query),
                        "period": ~Q(page__menu__year__range=query.split()),
                        "location": ~Q(page__menu__location__icontains=query),
                        "restaurant": ~Q(page__menu__restaurant__icontains=query)
                        }
        if neg:
            return neg_filter_keys[parameter]
        else:
            return filter_keys[parameter]


    def single_form(self, form):
        query = form[1]
        parameter = form[0]
        items = MenuItem.objects.select_related('dish.name','price','menupage__menu.restaurant','menupage__menu.year','menupage__menu.location','dish__classification.classification', 'menupage__menu.period').filter(self.get_fk(parameter, query))
        return items

    def multi_forms(self, forms):
        final_query = self.get_fk(forms[0][0], forms[0][1])
        for x in xrange(1,len(forms)):
            new_query = self.get_fk(forms[x][0], forms[x][1], forms[x-1][3])
            final_query = self.var_reduce(forms[x-1][2], [final_query, new_query])
        return MenuItem.objects.select_related('dish.name','price','menupage__menu.restaurant','menupage__menu.year','menupage__menu.location','dish__classification.classification', 'menupage__menu.period').filter(final_query)

    def process_form(self, form):
        query = form.get('query',None)
        parameter = form.get('parameter',None)
        bool_ = form.get('boolean',None)
        if bool_:
            bool_ = bool_.split()[0].lower()
            try:
                neg = bool(bool_.split()[1])
            except IndexError:
                neg = None
        else:
            bool_ = None
            neg = None
        return (parameter, query, bool_, neg)

    def render_search(self, request):
        formset = self.formset(request.GET)
        if formset.is_valid():
            forms = [self.process_form(form) for form in formset.cleaned_data if form.get('query',None) and form.get('parameter',None)]
#             return render(request, 'search2.html', {'formset':formset, 'items':None, 'submitted':True, 'forms':formset.cleaned_data})
            if not forms:
                return render(request, 'search2.html', {'formset':formset, 'items':None, 'submitted':True, 'forms':formset.cleaned_data})
            if len(forms) == 1:
                return render(request, 'search2.html', {'formset':formset, 'items':self.single_form(forms[0]), 'submitted':True, 'forms':forms})
            else:
                return render(request, 'search2.html', {'formset':formset, 'items':self.multi_forms(forms), 'submitted':True, 'forms':forms})
        else:
            return render(request, 'search2.html', {'formset':formset, 'errors':formset.errors, 'submitted':False})

    def dispatch(self, request):
        try:
            return self.render_search(request)
        except ValidationError:
            formset = self.formset()
            return render(request, 'search2.html', {'formset':formset, 'submitted':False})

# def search(request):
#     SearchFormset = formset_factory(SearchForm,extra=5)
#     if request.GET:
#         formset = SearchFormset(request.GET)
#         if formset.is_valid():
#             forms = []
#             req = formset.cleaned_data
#             for form in req:
#                 query = form.get('query',None)
#                 parameter = form.get('parameter',None)
#                 if query and parameter:
#                     filter_keys = {
#                         "dish-name":Q(dish__name__icontains=query),
#                         "regex":Q(dish__full_name__regex=r'{0}'.format(re.escape(query))),
#                         "course":Q(dish__classification__classification__iexact=query),
#                         "year":Q(page__menu__year__exact=query),
#                         "period":Q(page__menu__period__exact=query),
#                         "location":Q(page__menu__location__icontains=query),
#                         "restaurant":Q(page__menu__restaurant__icontains=query)
#                         }
#                     neg_filter_keys = {
#                         "dish-name": ~Q(dish__name__icontains=query),
#                         "regex": ~Q(dish__full_name__regex=r'{0}'.format(re.escape(query))),
#                         "course": ~Q(dish__classification__classification__iexact=query),
#                         "year": ~Q(page__menu__year__exact=query),
#                         "period": ~Q(page__menu__period__exact=query),
#                         "location": ~Q(page__menu__location__icontains=query),
#                         "restaurant": ~Q(page__menu__restaurant__icontains=query)
#                         }
#                     bool = form.get('boolean',None).split().lower()
#                     if len(bool) > 1:
#                         forms.append((neg_filter_keys[parameter],bool[0]))
#                     else:
#                         forms.append((filter_keys[parameter],bool[0]))
#             def var_reduce(op,slice):
#                 if op == "and":
#                     return reduce(operator.and_(x,y),slice)
#                 elif op == "or":
#                     return reduce(operator.or_(x,y),slice)
#             if len(forms) > 1:
#                 final_query = filter_keys[forms[0][0]]
#                 for x in xrange(1,len(forms)):
#                     try:
#                         slice = [final_query,filter_keys[forms[x][0]]]
#                         final_query = var_reduce(forms[x-][1],slice)
#                 items = MenuItem.objects.select_related('dish.name','dish__menuitem.formatted_price','dish__menuitem__menupage__menu.restaurant','dish__menuitem__menupage__menu.year','dish__menuitem__menupage__menu.location','dish__classification.classification').filter(final_query)
#             else:
#                 items = MenuItem.objects.select_related('dish.name','dish__menuitem.formatted_price','dish__menuitem__menupage__menu.restaurant','dish__menuitem__menupage__menu.year','dish__menuitem__menupage__menu.location','dish__classification.classification').filter(filter_keys[forms[0][0]])
#             return render(request, 'search2.html', {'formset':formset,'items':items, 'submitted':True})
#         else:
#             req = request.GET
#             return render(request, 'search2.html', {'formset':formset, 'errors':formset.errors, 'req':req, 'submitted':False})
#     formset = SearchFormset()
#     return render(request,'search2.html', {'formset':formset,'submitted':False})

# if request == "POST":
#       form = SearchForm(request.POST)
#       if form.is_valid():
#           data = formset.cleaned_data
#       else:
#           data = request.POST
#       return render(request, 'results.html', {'form':form, 'submitted':True, 'errors':form.errors, 'data':data, 'posted':'POST', 'valid':form.is_valid(), "search":'search' in request.POST})
#
#       data = {}
#       for k in request.META:
#           data[k] = request.META[k]
#       for k in request.GET:
#           if k in data.keys():
#               data["GET_{0}".format(k)] = request.GET[k]
#           else:
#               data[k] = request.GET[k]
#       for k in request.POST:
#           if k in data.keys():
#               data["POST_{0}".format(k)] = request.POST[k]
#           else:
#               data[k] = request.POST[k]
#       form = SearchForm()
#       return render(request,'search2.html', {'form':form, 'submitted':False, 'posted':'NONE', "data":data})
