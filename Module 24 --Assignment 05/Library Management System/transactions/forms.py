from django import forms
from .models import Transaction
class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount','account']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance = self.account.balance
        return super().save()

    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')  # user er fill korah form theke amara amount field er value ke niye aslam
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'you need to deposit at least {min_deposit_amount}$'
            )
        return amount