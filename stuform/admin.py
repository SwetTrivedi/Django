from django.contrib import admin
from . models import Lame
from . models import Modelinherit
# Register your models here.
@admin.register(Lame)
class LameAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')


######################################################################################################################
#this register is same form but data save in database two forms liike teacher and studwent

@admin.register(Modelinherit)
class ModelAdmin(admin.ModelAdmin):
    list_display=('id','student_name','teacher_name','email','password')

########################################################################################################################

#this register is massage framework
from . models import Messages
@admin . register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display=('id','student','email','password')
