from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    title = models.CharField(max_length=64)
    message = models.TextField(max_length=1000)
    created = models.DateTimeField("Date Submission", auto_now_add="True")
    updated = models.DateTimeField("Date Modification", auto_now="True")

    class Meta:
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"
