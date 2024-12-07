from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Products)
admin.site.register(Variants)
admin.site.register(SubVariants)
admin.site.register(Variant_type)
admin.site.register(SubVariant_types)