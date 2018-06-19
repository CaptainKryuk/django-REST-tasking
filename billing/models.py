from django.db import models
from base.models import AbstractDataTimeModel


class MoneyLog(AbstractDataTimeModel):
    """
    Record all actions with money
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    debit = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    credit = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    money = models.DecimalField(decimal_places=2, max_digits=7, default=0)

class TaskExpense(AbstractDataTimeModel):
    """
    Record all task actions
    """
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    executor = models.ForeignKey('users.User', on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=7, decimal_places=2)