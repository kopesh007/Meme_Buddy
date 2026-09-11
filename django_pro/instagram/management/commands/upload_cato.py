from django.core.management.base import BaseCommand

from instagram.models import cat

c=["Funny","Technnology","Biological","Industriyal","Bussinus","Study"]

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        for i in c:
            cat.objects.create(name=i)
        
        self.stdout.write(self.style.SUCCESS("Category has been Uploaded !!"))
