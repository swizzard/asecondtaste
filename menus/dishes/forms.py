from django import forms
from bootstrap_toolkit.widgets import BootstrapTextInput
import re

class SearchForm(forms.Form):
	def clean(self):
		if any(self.errors):
			return self.errors
		valid_courses = ["appetizer","main","dessert"]
		valid_period = re.compile(r'\d\d\d0-\d\d\d5|\d\d\d5-\d\d\d0')
		valid_year = re.compile(r'\d{4}')
		multi_rows = ["year","period","course"]
		cleaned_data = super(SearchForm, self).clean()
		query = cleaned_data.get("query")
		parameter = cleaned_data.get("parameter")
		if query and parameter:
			if parameter == "course" and query.lower() not in valid_courses:
				raise forms.ValidationError("{0} is not a valid course option.".format(query))
			if parameter == "period" and not re.match(valid_period,query):
				raise forms.ValidationError("{0} is not a properly formatted period. Valid five-year periods span either the first or second half of a decade. For example: 1910-1915, 1925-1930.".format(query))
			if parameter == "year" and not re.match(valid_year,query):
				raise forms.ValidationError("Please enter a four-digit year.")
		return cleaned_data
	__name__ = "searchform"
	name = 'dish-name'
	location = 'location'
	restaurant = 'restaurant'
	course = 'course'
	regex = 'regex'
	year = 'year'
	period = 'period'
	and_ = 'AND'
	or_ = 'OR'
	and_not = "AND NOT"
	or_not = "OR NOT"
	parameter_choices = (
		(name, "Dish Name"),
		(location, "Location"),
		(restaurant, "Restaurant"),
		(year, 'Year'),
		(period, 'Five-Year Period'),
		(course, "Course"),
		(regex, "Regular Expression"),
		)
	bool_choices = (
		(and_, "AND"),
		(or_,"OR"),
		(and_not, "AND NOT"),
		(or_not, "OR NOT"),
		)
	query = forms.CharField(max_length=255, widget=BootstrapTextInput)
	parameter = forms.ChoiceField(
		widget = forms.RadioSelect(attrs={"class":"parameter"}),
		choices = parameter_choices)
	boolean = forms.ChoiceField(
		widget = forms.RadioSelect(attrs={"class":"bool"}),
		choices = bool_choices,
		required = False)
