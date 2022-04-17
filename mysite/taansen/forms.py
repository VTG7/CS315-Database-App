from django import forms

class searchForm(forms.Form):
    title= forms.CharField(label='Search by song', max_length=100, required = False) # consider shifting to text field since our song database had a textfield as its title input. 
    #CHOICES = [('choice1','with'),
     #    ('choice2','without')]
    Selector = forms.BooleanField(widget= forms.CheckboxInput, required=False) # consider shifting to text field since our song database had a textfield as its title input. 
    artist= forms.CharField(label='Search by artist', max_length=100, required = False) # consider shifting to text field since our song database had a textfield as its title input. 
    Selector2 = forms.BooleanField(widget= forms.CheckboxInput, required=False) # consider shifting to text field since our song database had a textfield as its title input. 
    actor = forms.CharField(label='Search by actor', max_length=100, required = False) # consider shifting to text field since our song database had a textfield as its title input. 
    Selector3 = forms.BooleanField(widget= forms.CheckboxInput, required=False) # consider shifting to text field since our song database had a textfield as its title input. 
    genre = forms.CharField(label='Search by genre', max_length=100, required = False) # consider shifting to text field since our song database had a textfield as its title input. 
    Selector4 = forms.BooleanField(widget= forms.CheckboxInput, required=False) # consider shifting to text field since our song database had a textfield as its title input. 
    lyrics = forms.CharField(label='Search by lyrics', max_length=200, required = False, widget=forms.Textarea) # consider shifting to text field since our song database had a textfield as its title input. 
