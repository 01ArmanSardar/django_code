# from django.contrib import admin
# from .models import Transaction
# # Register your models here.
# admin.site.register(Transaction)

from django.contrib import admin

# from transactions.models import Transaction
from .models import Transaction
from .views import Transaction_mail
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()
        Transaction_mail(obj.account.user,'admin_email.html',"Loan Approval",obj.amount)
        super().save_model(request, obj, form, change)