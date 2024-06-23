from django import forms
from .models import Transaction
 
class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['amount','transaction_type']

    def __init__(self,*args,**kwargs):
        self.account=kwargs.pop('acount')
        super().__init__(*args,**kwargs)
        self.fields['transaction_type'].disabled=True #ei feild disable takbhe
        self.fields['transaction_type'].widget=forms.HiddenInput() # user tekeh hide korah takbhe

    def save(self,commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()
    


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount=100
        Amount=self.cleaned_data.get('amount')#user er fill korah form theke amara amount field er value ke niye aslam
        if Amount<min_deposit_amount:
            raise forms.ValidationError(
                f'you need to deposit at least {min_deposit_amount}$'
            )
        return Amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account=self.account
        min_withdraw_amount=500
        max_withdraw_amount=20000
        balance=account.balance
        Amount=self.cleaned_data.get('amount')
        if Amount<min_withdraw_amount:
            raise forms.ValidationError(
            f'you can withdraw at least{min_withdraw_amount}'
        )
        if Amount>max_withdraw_amount:
            raise forms.ValidationError(
                f'you can wthdraw at most {max_withdraw_amount}'
            )
        if Amount>balance:
            raise forms.ValidationError(
                f"you balance is {balance}you can not withdraw more than your account balance"
            )
        return Amount
        

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        Amount=self.cleaned_data.get('amount'
        )
        return Amount