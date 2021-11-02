from django.contrib.auth.models import User
from django.db import models
from main.models import News, Laws, Publication
# Create your models here.

class FavouriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FavouriteLaws(models.Model):
    news = models.ForeignKey(Laws, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavouritePublication(models.Model):
    news = models.ForeignKey(Publication, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)