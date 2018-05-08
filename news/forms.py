from django import forms
#we create a class that inherits from forms module we imported
class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label='First Name',max_length=30)
    email=forms.EmailField(label='Email')
