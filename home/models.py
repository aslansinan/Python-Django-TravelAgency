from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


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
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed','Closed')
    )
    name = models.CharField(max_length=20)
    email = models.CharField(blank=True,max_length=55)
    subject = models.CharField(blank=True, max_length=255)
    message = models.CharField(blank=True, max_length=30)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
        class Meta:
            model = ContactFormMessage
            fields = {'name','email','subject','message'}
            widgets = {
            'name' : TextInput(attrs={'class':'input','placeholder':'Name-Surname'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'emil': TextInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'TourMessage','rows':'5'}),
            }