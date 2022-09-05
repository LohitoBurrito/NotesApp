from django.contrib import admin
from .models import fileUploadG, fileUploadL, fileUploadB, graingerMajor, lasMajor, giesMajor
from .models import contributors
# Register your models here.

admin.site.register(graingerMajor)
admin.site.register(giesMajor)
admin.site.register(lasMajor)
admin.site.register(fileUploadG)
admin.site.register(fileUploadL)
admin.site.register(fileUploadB)
admin.site.register(contributors)

