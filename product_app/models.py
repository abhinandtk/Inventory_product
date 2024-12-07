from django.db import models
import uuid
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Products(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ProductID=models.BigIntegerField(unique=True)
    ProductCode=models.CharField(max_length=225,unique=True)
    ProductName=models.CharField(max_length=225)
    ProductImage=VersatileImageField(upload_to="uploads/",blank=True,null=True)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    UpdatedDate=models.DateTimeField(blank=True,null=True)
    CreatedUser=models.ForeignKey("auth.User",related_name="user%(class)s_objects",on_delete=models.CASCADE)
    IsFavourite=models.BooleanField(default=False)
    Active=models.BooleanField(default=True)
    HSNCode=models.CharField(max_length=225,blank=True,null=True)
    TotalStock=models.DecimalField(default=0.00,max_digits=20,decimal_places=8,blank=True,null=True)
     
    class Meta:
        db_table="products_product"
        verbose_name="product"
        verbose_name_plural = "products"
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")

class Variants(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product=models.ForeignKey(Products,related_name="variants",on_delete=models.CASCADE)
    name=models.CharField(max_length=225)

    class Meta:
        db_table="product_variants"
        unique_together=("product","name")

class SubVariants(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    variant=models.ForeignKey(Variants,related_name="subvariants",on_delete=models.CASCADE)
    options=models.CharField(max_length=225)

    class Meta:
        db_table="products_subvariants"
        unique_together=("variant","options")