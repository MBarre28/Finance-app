from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def remaining(self):
        return self.amount - self.spent

    def __str__(self):
        return f"{self.name} (${self.amount})"

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def progress_percent(self):
        if self.target_amount == 0:
            return 0
        return (self.saved_amount / self.target_amount) * 100

    def __str__(self):
        return f"{self.title} (${self.saved_amount}/${self.target_amount})"