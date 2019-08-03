from django.contrib import admin
from wagtail.contrib.modeladmin.options import( 
    modeladmin_register,
    ModelAdmin,
    )

from .models import Subsribers
# Register your models here.
class SubsriberAdmin (ModelAdmin) :
    model = Subsribers
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings = False
    exclude_from_explorer = False
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")

modeladmin_register (SubsriberAdmin)