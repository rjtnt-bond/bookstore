from django.contrib import admin
from book.models import BookStoreModel,Studentinfo,Teacherinfo,Person,Passport,Friend,me,EmployeeModel,ManagerModel
      

# Register your models here.
class BookstoreAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','catgory','first_pub','last_pub')
admin.site.register(BookStoreModel,BookstoreAdmin)




admin.site.register(Studentinfo)
admin.site.register(Teacherinfo)


#one to one relationship


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','city','designation')
admin.site.register(EmployeeModel,EmployeeAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display=('id','name','city','designation','take_interview','hiring')
admin.site.register(ManagerModel,ManagerAdmin)


class FriendModelAdmin(admin.ModelAdmin):
    list_display=('id','school','attendence','hw','section') 
admin.site.register(Friend,FriendModelAdmin)

@admin.register(me)
class MeModelAdmin(admin.ModelAdmin):
    list_display=('id','school','attendence','hw','section') 



class PersonModelAdmin(admin.ModelAdmin):
    list_display=['name','city','email']
admin.site.register(Person,PersonModelAdmin)

class PassportAdmin(admin.ModelAdmin):
    list_display=['user','page','validity']
admin.site.register(Passport,PassportAdmin)