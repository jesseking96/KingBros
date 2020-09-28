from django import forms

class ContactForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea)
