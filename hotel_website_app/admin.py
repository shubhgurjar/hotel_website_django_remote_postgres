from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "customer_msg")
    search_fields = ("customer_name", "customer_email")
    list_filters = ("customer_email",)
    ordering = ("customer_name",)
    readonly_fields = ("customer_name", "customer_email")



# Register your models here.
admin.site.register(Customer, CustomerAdmin)
