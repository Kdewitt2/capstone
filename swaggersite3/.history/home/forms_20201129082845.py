from django import forms
from .models import Order, Product
from django.contrib.auth.models import User


class OrderModelForm(forms.ModelForm):
    fields = ['GrapefruitSoap', 
            'LemongrassSugarScrub', 
            'CharcoalClayFacialScrub', 
            'LavenderSoap',
            'AloeVeraGoatMilkSoap', 
            'PeppermintSoap', 
            'EucalyptusSoap', 
            'RawSoap', 
            'CalendulaBurdockSalve', 
            'SootheMeSalve', 
            'LavenderLoofahSoap', 
            'LemonPoppySeedSoap']
    orderDetails = {}

    class Meta:
        model = Order
        user = User
        fields = ['GrapefruitSoap', 
            'LemongrassSugarScrub', 
            'CharcoalClayFacialScrub', 
            'LavenderSoap',
            'AloeVeraGoatMilkSoap', 
            'PeppermintSoap', 
            'EucalyptusSoap', 
            'RawSoap', 
            'CalendulaBurdockSalve', 
            'SootheMeSalve', 
            'LavenderLoofahSoap', 
            'LemonPoppySeedSoap']

    def save(self, commit=True):
        instance = super().save(commit)

        instance.orderDetails.add(self.cleaned_data['GrapefruitSoap'])
        instance.orderDetails.add(self.cleaned_data['LemongrassSugarScrub'])
        instance.orderDetails.add(self.cleaned_data['CharcoalClayFacialScrub'])
        instance.orderDetails.add(self.cleaned_data['LavenderSoap'])
        instance.orderDetails.add(self.cleaned_data['AloeVeraGoatMilkSoap'])
        instance.orderDetails.add(self.cleaned_data['PeppermintSoap'])
        instance.orderDetails.add(self.cleaned_data['EucalyptusSoap'])
        instance.orderDetails.add(self.cleaned_data['RawSoap'])
        instance.orderDetails.add(self.cleaned_data['CalendulaBurdockSalve'])
        instance.orderDetails.add(self.cleaned_data['SootheMeSalve'])
        instance.orderDetails.add(self.cleaned_data['LavenderLoofahSoap'])
        instance.orderDetails.add(self.cleaned_data['LemonPoppySeedSoap'])

        return instance
        
