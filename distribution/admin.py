from django.contrib import admin
from distribution.models import *
# Register your models here.
admin.site.register(Route)
admin.site.register(RouteRelation)
admin.site.register(GoodState)
admin.site.register(TobaccoGood)
admin.site.register(Order)
admin.site.register(OrderContent)
