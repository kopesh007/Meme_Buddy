from django import forms

class check_post(forms.Form):
    image = forms.ImageField(label="Image",required=True,max_length=500)
    caption = forms.CharField(label="Description",required=True,max_length=500)
    cato = forms.IntegerField(label="Category",required=True)

