from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    category_id = models.IntegerField()
    description = models.CharField(max_length=1024)
    picture_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_news'

class Category(models.Model):
    name = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_category'