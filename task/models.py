from django.db import models
from base.models import AbstractDataTimeModel


class Task(AbstractDataTimeModel):
    assignee = models.ForeignKey('users.User', related_name='assignee', on_delete=models.CASCADE)
    created_by = models.ForeignKey('users.User', related_name='created_by', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
