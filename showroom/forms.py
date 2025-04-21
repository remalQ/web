from django import forms
from models import Sale, TradeINDeal


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['car', 'is_tradein', 'contract_file']


class TradeINForm(forms.ModelForm):
    class Meta:
        model = TradeINDeal
        fields = ['old_car_description', 'new_car', 'valuation', 'final_price']
