from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATGORY=(
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id =models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    catgory=models.CharField(max_length=20,choices=CATGORY)
    first_pub=models.DateTimeField(auto_now_add=True)#ekdom first date aita 
    last_pub=models.DateTimeField(auto_now=True)#tarpor jjoto par update hobe tar date aita
        
#abstract model example 
class CommonInfo(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=50)
    class Meta:
        abstract=True
        
class Studentinfo(CommonInfo):
    section=models.CharField(max_length=30)
    payment=models.IntegerField()
    
class Teacherinfo(CommonInfo):
    department=models.CharField(max_length=30)
    salary=models.IntegerField()

    

# Malti Table  model inheritance
class EmployeeModel(models.Model):
    name=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    designation=models.CharField(max_length=40,null=True)
    
class ManagerModel(EmployeeModel):
    take_interview=models.BooleanField(null=True)
    hiring=models.BooleanField(null=True)      
    
# proxy Model
class Friend(models.Model):# friend class a ace o amr hoa kaj korbe 
    school=models.CharField(max_length=30)
    section=models.CharField(max_length=30)
    attendence=models.BooleanField(max_length=30)
    hw=models.CharField(max_length=50)
    
class me(Friend):# ami class ea nai 
    class Meta:
        proxy=True
        ordering=['id']
        
        
#one to one relationship

class Person(models.Model): 
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    
class Passport(models.Model):
    user=models.OneToOneField(to=Person,on_delete=models.CASCADE)
    pass_number=models.IntegerField(default = None)
    page=models.IntegerField(default = None)
    validity=models.IntegerField(default = None)


        