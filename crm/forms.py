from django import forms

class Orderform(forms.Form):
    
    name = forms.CharField(max_length=200,required = False) # required =False qilsak kerakmas polyani tuldirmasdan junatish m-n
    phone = forms.CharField(max_length=200)
    