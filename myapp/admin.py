from django.contrib import admin
from.models import StudentCallList



class StudentCallListAdmin(admin.ModelAdmin):
    list_display = ('Your_Name', 'Email', 'Mobile_No', 'City', 'College_Name', 'Department')

admin.site.register(StudentCallList, StudentCallListAdmin)


