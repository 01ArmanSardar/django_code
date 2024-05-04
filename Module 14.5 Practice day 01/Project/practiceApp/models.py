from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    # auto_field=models.AutoField(primary_key=True)
    # big_integerFeild=models.BigIntegerField()
    # binaryFeild=models.BinaryField()
    # booleanFeild=models.BooleanField()
    charFeild=models.CharField(max_length=30)
    # dateFeild=models.DateField()
    # dateTimeFeild=models.DateTimeField()
    # decimalFeild=models.DecimalField(max_digits=5, decimal_places=5)
    emailFeild=models.EmailField()
