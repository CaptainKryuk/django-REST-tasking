from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    customer = 1
    executor = 2

    USER_TYPES = (
        (customer, _(u"Заказчик")),
        (executor, _(u"Исполнитель")),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=executor)
    balance = models.DecimalField(decimal_places=2, max_digits=7)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def update_balance(self, reason, **kwargs):
        pass
