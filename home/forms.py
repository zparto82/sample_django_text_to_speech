from django import forms 
    
 
class InputForm(forms.Form):   
    text = forms.CharField(max_length = 200) 
