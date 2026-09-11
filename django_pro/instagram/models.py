from django.db import models

class Posts(models.Model):
    caption=models.CharField(max_length=500)
    image = models.ImageField(null=True,upload_to="Posts/images",max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
        


# Create your models here.
