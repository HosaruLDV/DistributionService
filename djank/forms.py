from django import forms
from djank.models import Client, Message, DistributionList


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class DistributionForm(forms.ModelForm):
    class Meta:
        model = DistributionList
        exclude = ['owner']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
