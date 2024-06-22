from django.shortcuts import render,HttpResponse
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm,WithdrawForm,LoanRequestForm
from django.contrib import messages
from .constants import DEPOSIT,WITHDRAWL,LOAN,LOAN_PAID
from datetime import datetime
# Create your views here.

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name=''
    model=Transaction
    title=''
    success_url=''

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update(
            {
                'acount':self.request.user.account,
            }
        )
        return kwargs
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update(
            {
              'title'  :self.title
            }
        )

class DepositMoneyView(TransactionCreateMixin):
    form_class=DepositForm
    title="Deposit"

    def get_initial(self):
        inital={'transaction_type':DEPOSIT}
        return inital
    
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance+=amount#user er kaceh ache 500 taka ,ami deposit korlam 1000 tk taile total balance hocche 1500
        account.save(
            update_fields=['balance']
        )
        messages(self.request,f'{amount} was deposited to your account')
        return super().form_valid(form)
    

class WithdrawMoneyView(TransactionCreateMixin):
    form_class=WithdrawForm
    title="WithdrawForm"

    def get_initial(self):
        inital={'transaction_type':WITHDRAWL}
        return inital
    
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance-=amount#user er kaceh ache 1500 taka ,ami withdraw korlam 1000 tk taile total balance hocche akhn 500
        account.save(
            update_fields=['balance']
        )
        messages(self.request,f'{amount} was withdraw to your account')
        return super().form_valid(form)
    



class LoanRequestView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title="Request for Loan"

    def get_initial(self):
        inital={'transaction_type':LOAN}
        return inital
    
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=Transaction.objects.filter(account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        if current_loan_count >=3:
            return HttpResponse("you have crossed your limits")
        messages(self.request,f'loan request for{amount} was succesfully sent in admin')
        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin,ListView):
    template_name=""
    model=Transaction
    balance=0

    def get_queryset(self):
        # jodi user kono type filter na kore taile tar total transaction report dekabo
        queryset=super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str,"%y-%m-%d").date()
            end_date=datetime.strptime(end_date_str,"%y-%m-%d").date()
            # queryset=queryset.filter(timestamp_date_gte=start_date,timestamp_date_lte=end_date)
            self.balance=Transaction.objects.filter(timestamp_date_gte=start_date,timestamp_date_lte=end_date).aggregate(sum('amount'))['amount__sum']
        
        else:
            self.balance=self.request.user.account.balance
        return queryset.distinct()
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update(
            {
              'account'  :self.request.user.account
            }
        )
        return context