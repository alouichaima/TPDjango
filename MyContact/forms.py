from django import forms

from MyContact.models import Contact

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class contactform3(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('firstname','lastname','email','message')