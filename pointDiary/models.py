from django.contrib.gis.db import models

# Create your models here.
class Diary(models.Model):
    #field definitions
    title = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True) 
    text = models.TextField()
    loc = models.PointField()
    user = models.TextField()
   
    def __unicode__(self):
        return self.title

 
