from django import forms
from .models import *

class DetalForm(forms.ModelForm):

    class Meta:
        model = Detal
        fields = ('catalog_number', 'alternativ_number', 'naimenovanie', 'opisanie',)
        labels ={
            'catalog_number' : 'Каталожный номер:',
            'alternativ_number' : 'Альтернативный номер:',
            'naimenovanie': 'Наименование',
            'opisanie' : 'Описание:',

        	}
#fields = ('Каталожный номер:', 'Альтернативный номер:', 'Описание:',)
    

class TestForm(forms.ModelForm):
    
	class Meta:
		model = SearchNumb
		fields =('val',)


class SearchForm(forms.Form):
	search_number = forms.CharField(label='Введите код детали:', max_length=100)




class SearchCAT(forms.Form):
	search_category = forms.CharField(label='Введите категорию детали:', max_length=100)