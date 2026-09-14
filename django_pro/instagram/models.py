from django.db import models
from django.utils.text import slugify


class cat(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Posts(models.Model):
    caption=models.CharField(max_length=500)
    image = models.ImageField(null=True,upload_to="Posts/images",max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    cato = models.ForeignKey(cat,on_delete=models.CASCADE,default=1)
    sl = models.SlugField(unique=True,)

    def select_image(self):
        url = self.image if self.image.__str__().startswith(("http://","https://")) else self.image.url
        return url

    def save(self,*args,**kwargs):
        self.sl = slugify(self.image)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.caption



# Create your models here.
