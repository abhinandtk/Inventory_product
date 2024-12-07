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
    def __str__(self):
        return self.ProductName

class Variant_type(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=225,unique=True)
    class Meta:
        db_table = "variant_types"
        verbose_name = "Variant Type"
        verbose_name_plural = "Variant Types"
    def __str__(self):
        return self.name

class Variants(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product=models.ForeignKey(Products,related_name="variants",on_delete=models.CASCADE)
    variant_type=models.ForeignKey(Variant_type,related_name="variants",on_delete=models.CASCADE)


    class Meta:
        db_table="product_variants"
        unique_together=("product","variant_type")
    def __str__(self):
        return self.variant_type.name

class SubVariant_types(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=225,unique=True)
    variant_type=models.ForeignKey(Variant_type,related_name="subvariant_types",on_delete=models.CASCADE)
    class Meta:
        db_table = "subvariant_types"
        verbose_name = "Subvariant Type"
        verbose_name_plural = "Subvariant Types"
    def __str__(self):
        return self.name

class SubVariants(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    variant=models.ForeignKey(Variants,related_name="subvariants",on_delete=models.CASCADE)
    options=models.ForeignKey(SubVariant_types,related_name="subvariants",on_delete=models.CASCADE)
    # stock = models.IntegerField(default=0)  # Track stock here

    class Meta:
        db_table="products_subvariants"
        unique_together=("variant","options")
    def __str__(self):
        return self.options.name



