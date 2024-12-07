from rest_framework import serializers
from .models import *

class SubVarientSerializer(serializers.ModelSerializer):
    subvariant_name = serializers.CharField(source="options.name", read_only=True)  # Expose the name in the response

    class  Meta:
        fields=['id','options','subvariant_name']
        model=SubVariants
        extra_kwargs={
   'options': {'write_only': True} 
        }
 

class VarientSerializer(serializers.ModelSerializer):
    subvariants=SubVarientSerializer(many=True)
    variant_name = serializers.CharField(source="variant_type.name", read_only=True)  # Expose the name in the response
    class Meta:
        fields=['id','subvariants','variant_type','variant_name']
        model=Variants
    extra_kwargs = {
        'product': {'read_only': True},
        'variant_name':{'read_only':True},
        'variant_type': {'write_only': True} 
    }
class ProductSerializer(serializers.ModelSerializer):
    variants=VarientSerializer(many=True)
    class Meta:
        fields=['id', 'ProductID', 'ProductCode', 'ProductName','ProductImage','CreatedDate','UpdatedDate','CreatedUser','IsFavourite','Active','HSNCode','TotalStock','variants']
        model=Products

    def create(self,validated_data):
            variants_data=validated_data.pop('variants')
            product=Products.objects.create(**validated_data)
            for variant_data in variants_data:
                subvariants_data = variant_data.pop('subvariants') 
                variant=Variants.objects.create(product=product,**variant_data)

                for subvariant_data in subvariants_data:
                    SubVariants.objects.create(variant=variant, **subvariant_data)
            return product