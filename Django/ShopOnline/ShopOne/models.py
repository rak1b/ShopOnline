from django.db import models


class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="shop/imgs")

    def __str__(self):
        return self.product_name



#
