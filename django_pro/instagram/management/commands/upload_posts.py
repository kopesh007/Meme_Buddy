from django.core.management.base import BaseCommand
import random
from instagram.models import Posts,cat
img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
        ]
caption=["DAAAAAAAAAAAAAAAII","SSSOOOOOOOOOOOOOOOOOOOOOOOO","MITTAAAAAAAAAAAAAAAAAAAAAIIII","PULAAAAAAAAAAAAAAAAAAAAAAAAAAA"]

class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        Posts.objects.all().delete()
        cate= cat.objects.all()

        for i,j in zip(caption,img_urls):
            c = random.choice(cate)

            Posts.objects.create(caption=i,cato=c,image=j)
        self.stdout.write(self.style.SUCCESS("Posts Data has been Uploaded !! "))
