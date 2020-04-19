from django.contrib import admin
from demo.models import Book,Number,Character,Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["Title","Description","Status","Price","number"]
    list_display= ["Title","Price"]
    list_filter=['Published']
    search_fields=["Title"]

@admin.register(Number)
class BookNumber(admin.ModelAdmin):
    fields=["bal1"]

# @admin.register(Character)
# class CharacterAdmin(admin.ModelAdmin):
#     fields=["name",]

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fields = ["name","book"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["name","surname","books"]


