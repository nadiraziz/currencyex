from django.db import models
import uuid


# services
class Services(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    featured_image = models.ImageField(
        default='default/default.jpg', null=True, blank=True, upload_to='services/'
    )

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img


# news
class News(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    news_title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        default='default/default.jpg', null=True, blank=True, upload_to='news/'
    )

    def __str__(self):
        return str(self.news_title)

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_no = models.CharField(max_length=200, null=True, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email
