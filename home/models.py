from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(blank=True,max_length=255)
    company= models.CharField(blank=True,max_length=30)
    address= models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=30)
    fax = models.CharField(blank=True,max_length=30)
    email = models.CharField(blank=True,max_length=30)
    smtpserver = models.CharField(blank=True,max_length=30)
    smtpemail = models.CharField(blank=True,max_length=30)
    smtppassword = models.CharField(blank=True,max_length=30)
    smtpport = models.CharField(blank=True,max_length=8)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=30)
    instagram = models.CharField(blank=True,max_length=30)
    twitter = models.CharField(blank=True,max_length=30)
    aboutus = models.TextField()
    contact = models.TextField()
    references = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


