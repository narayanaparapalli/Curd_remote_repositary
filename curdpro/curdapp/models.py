from django.db import models
class ProductData(models.Model):
    p_id=models.IntegerField()
    p_name=models.CharField(max_length=50)
    p_cost=models.IntegerField()
    p_color=models.CharField(max_length=50)
    p_class=models.CharField(max_length=50)
    c_name=models.CharField(max_length=50)
    c_mobile=models.BigIntegerField()
    c_email=models.EmailField(max_length=100)

