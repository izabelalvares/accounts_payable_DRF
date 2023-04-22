from django.db import models



class Invoice(models.Model):
    company = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.invoice_number
    