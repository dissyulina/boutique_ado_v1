from django.contrib import admin
from .models import Order, OrderLineItem


# this class is going to inherit from admin.TabularInline
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    # fields that will be calculated by our model methods, can't be editted
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    # this will allow us to specify the order of the fields in the admin interface
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    # to restrict the columns that show up in the order list to only a few key items
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # set them to be ordered by date in reverse order
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)