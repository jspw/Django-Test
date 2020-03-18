from django.contrib import admin
from first_app.models import Topic,AccessRecord,Webpage

# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
