from django import forms

class searchForm(forms.Form):
    query = forms.CharField(label='Your Query', max_length=100) # consider shifting to text field since our song database had a textfield as its title input. 
