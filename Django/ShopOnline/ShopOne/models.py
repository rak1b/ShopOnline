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

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField( max_length=254)
    contact_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_name


class checkout_info(models.Model):
    checkout_id = models.AutoField(primary_key=True)
    checkout_name = models.CharField(max_length=90)
    checkout_phone = models.IntegerField(max_length=15)
    checkout_email = models.EmailField( max_length=254)
    checkout_address = models.CharField(max_length=200)
    checkout_zip_code = models.CharField(max_length=10)
    checkout_json = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.checkout_id)



#
