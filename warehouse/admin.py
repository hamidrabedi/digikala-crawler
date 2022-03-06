from django.contrib import admin

from warehouse.models import(
    Product,
    Pack,
    Color,
    Guarantee
)

class PackAdminInline(admin.StackedInline):
    model = Pack
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[
        'sku',
        'title',
        'packs'
    ]
    save_on_top = True
    empty_value_display = '-N/A-'
    inlines = [PackAdminInline]

    def packs(self, obj):
        return ', '.join([str(pack.id) for pack in obj.packs.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('packs')

@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display=[
        'product',
        'price',
        'guarantee',
        'color'
    ]
    list_editable = ['price']
    raw_id_fields = [
        'product',
        'guarantee',
        'color'
    ]


@admin.register(Color)
class ColorAadmin(admin.ModelAdmin):
    list_display=[
        'title'
    ]

@admin.register(Guarantee)
class GuaranteeAdmin(admin.ModelAdmin):
    list_display=[
        'title'
    ]