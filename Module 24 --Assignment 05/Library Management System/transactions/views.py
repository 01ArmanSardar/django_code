from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy
from django.db.models import Sum
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from Core.models import Account
# Create your views here.


class DepositMoneyView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = DepositForm
    template_name = 'deposit.html'
    success_url = reverse_lazy('homepage')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print('some')
        kwargs.update(
            {
                'account': self.request.user.account,
            }
        )
        print(self.request.user.account)
        return kwargs
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        print('check deposit')
        Account = self.request.user.account
        Account.balance += amount  # Update the account balance
        Account.save(update_fields=['balance'])
        messages.success(self.request, f'{amount} was deposited to your account')

        # Send transaction email
        # Transaction_mail(self.request.user, 'deposit_email.html', "Deposit Message", amount)

        return super().form_valid(form)