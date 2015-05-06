from django.db import models


class User(models.Model):

    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)

    class Meta:
        db_table = 'users'
