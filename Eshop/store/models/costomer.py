from django.db import models


class Costomer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()






