from django.db import models

class Base(models.Model):
    prdid = models.IntegerField(primary_key=True)
    prdname = models.CharField(max_length=20)
    
    class Meta:
        abstract = True
        
class Child(Base):
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.prdname
    
class Base2(models.Model):
    
    prdid = models.IntegerField(primary_key=True)
    prdname = models.CharField(max_length=10)
    
class Child2(Base2):
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
class ProxyPost(Post):
    
    class Meta:
        proxy = True
        ordering = ["title"]
        