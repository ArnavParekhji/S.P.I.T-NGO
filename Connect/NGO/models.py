from django.db import models

class City(models.Model):
    name = models.CharField(max_length=120)

class NGO(models.Model):
    CATEGORIES = [
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Children', 'Children'),
        ('Senior Citizens', 'Senior Citizens'),
        ('Others', 'Others')
    ]

    name = models.CharField(max_length=250)
    cause = models.TextField()
    cities = models.ManyToManyField(City)
    description = models.TextField()
    website_link = models.URLField(max_length=520)
    logo = models.ImageField(upload_to='NGOs/Logos')
    categories = models.CharField(max_length=100, choices=CATEGORIES)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)

class Similar(models.Model):
    # This will store the id of the NGO and then store the ngos that are similar to that ngo
    prime_ngo = models.CharField(max_length=24)
    similar_ngo = models.ForeignKey(NGO, on_delete=models.DO_NOTHING)