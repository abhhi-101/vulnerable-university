from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

class TestAuth(models.Model):
    user = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    
'''c = TestAuth(user='user', passwd="passwd")
c.save()'''

'''result = Company.objects.raw("SELECT id, age FROM students_company WHERE company_name='Abhhi'")
result_list = list(result)
print(result_list)'''
'''for c in result:
    print(c.id, c.age)'''
'''for e in Company.objects.raw("SELECT id, age FROM students_company WHERE company_name='Abhhi'"):
    print(e.age)'''