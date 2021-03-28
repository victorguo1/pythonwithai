from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    primaryCategory = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    mainimage = models.ImageField(upload_to="products/", blank=True)
    name = models.CharField(max_length = 300)
    slug = models.SlugField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    detail_text = models.TextField(max_length=1000, verbose_name="Details")
    preview_text = models.TextField(max_length=200,verbose_name="Preview")
    price = models.FloatField()

    def __str__(self):
        return self.name