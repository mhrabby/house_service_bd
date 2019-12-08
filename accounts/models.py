from django.db import models


class Animals(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    food = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    nid = models.CharField(max_length=50, blank=True, null=True)
    upload_nid = models.ImageField(upload_to='media/')
    pic = models.ImageField(upload_to='media/')
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    type_of_work = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


STATUS = (
    ('pending', 'Pending'),
    ('accpeted', 'Accepted'),
    ('complete', 'Completed')
)


class Booking(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    nid = models.CharField(max_length=50, blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default='pending', blank=True, null=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Booking'

    def __str__(self):
        if self.name is None:
            return "ERROR-COMMON NAME IS NULL"
        return self.name
