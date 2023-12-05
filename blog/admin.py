from django.contrib import admin
from .models import Cloth
from .models import Outfit
from .models import Shoes
# Register your models here.
admin.site.register(Outfit)
admin.site.register(Cloth)
admin.site.register(Shoes)
