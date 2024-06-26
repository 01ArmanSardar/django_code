from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm,WithdrawForm,LoanRequestForm
from django.contrib import messages
from .constants import DEPOSIT,WITHDRAWL,LOAN,LOAN_PAID
from datetime import datetime
from django.urls import reverse_lazy
from django.db.models import Sum
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.


def Transaction_mail(user,template,subject,amount):
        message=render_to_string(template,{
            'user':user,
            'amount':amount,
        })
        
        send_email=EmailMultiAlternatives(subject,'',to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()
class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name='transaction_form.html'
    model=Transaction
    title=''
    success_url=reverse_lazy('Transaction_report')

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
        return context

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
        messages.success(self.request,f'{amount} was deposited to your account')

        # mail_subject="Deposite Message"
        # message=render_to_string('deposit_email.html',{
        #     'user':self.request.user,
        #     'amount':amount,
        # })
        # to_email=self.request.user.email
        # send_email=EmailMultiAlternatives(mail_subject,'',to=[to_email])
        # send_email.attach_alternative(message,'text/html')
        # send_email.send()

        Transaction_mail(self.request.user,'deposit_email.html',"Deposit Message",amount)
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
        if account.isBankRupt==False:
            account.balance-=amount#user er kaceh ache 1500 taka ,ami withdraw korlam 1000 tk taile total balance hocche akhn 500
            account.save(
                update_fields=['balance']
                )
            messages.warning(self.request,f'{amount} was withdraw to your account')
        else:
            messages.warning(self.request,f'Bankrupt')
        Transaction_mail(self.request.user,'deposit_email.html',"Withdrawl Message",amount)
        return super().form_valid(form)
    



class LoanRequestView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title="Request For Loan"

    def get_initial(self):
        inital={'transaction_type':LOAN}
        return inital
    
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=Transaction.objects.filter(account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        if current_loan_count >=3:
            return HttpResponse("you have crossed your limits")
        messages.success(self.request,f'loan request for{amount} was succesfully sent in admin')
        
        Transaction_mail(self.request.user,'loan_request_email.html',"Loan Request",amount)
        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin,ListView):
    template_name="transaction_report.html"
    model=Transaction
    balance=0
    context_object_name="Report_list"

    def get_queryset(self):
        # jodi user kono type filter na kore taile tar total transaction report dekabo
        queryset=super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str,"%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str,"%Y-%m-%d").date()
            queryset=queryset.filter(timestamp__date__gte=start_date,timestamp__date__lte=end_date)
            self.balance=Transaction.objects.filter(timestamp__date__gte=start_date,timestamp__date__lte=end_date).aggregate(Sum('amount'))['amount__sum']
        
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
    
class PayLoanView(LoginRequiredMixin,View):
    def get(self,request,loan_id):
        loan=get_object_or_404(Transaction,id=loan_id)

        if loan.loan_approve:
            user_account=loan.account
            if loan.amount<user_account.balance:
                user_account.balance-=loan.amount
                loan.balance_after_transaction=user_account.balance
                user_account.save()
                loan.transaction_type=LOAN_PAID
                loan.save()
                return redirect('loan_list')
            else:
                messages.error(self.request,f'loan amount is greater than avilable Balance')
                return redirect('loan_list')
            

class LoanListView(LoginRequiredMixin,ListView):
    model=Transaction
    template_name="loan_request.html"
    context_object_name="loans"
    def get_queryset(self):
        user_account=self.request.user.account
        queryset=Transaction.objects.filter(account=user_account,transaction_type=LOAN)
        return queryset
