from django.contrib import admin

from .models import FlexiAdmin,Employee,Register,Project,Creat,Applied,TActivies

admin.site.register(FlexiAdmin);#admin
admin.site.register(Employee);#employee
admin.site.register(Register);#user interns registerations
admin.site.register(Project);#project details (done by user)
admin.site.register(Creat);#peoject creation by project manager
admin.site.register(Applied);#peoject creation by project manager
admin.site.register(TActivies);#peoject creation by project manager
