from django import forms
from .models import PasswordEntry
from .models import TheUserEntry
from .models import ZhangDna


class PasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['website', 'username', 'password']


class theuserForm(forms.ModelForm):
    class Meta:
        model = TheUserEntry
        fields = ['theusername', 'thepassword']


class ZhangDnaForm(forms.ModelForm):
    class Meta:
        model = ZhangDna
        fields = ['Shouzhi', 'Leixing', 'Jiage']


from .models import Notebook


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['title', 'content']


from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'company', 'notes']



from django import forms
from .models import Addresss

class AddressForm(forms.ModelForm):
    class Meta:
        model = Addresss
        fields = ['name', 'phone', 'area', 'address', 'is_default']