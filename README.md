# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![image](https://github.com/Suresh-2006/ORM/assets/149347611/e908bd27-9cf3-4f2d-bf29-88dfc45f7931)
## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
model.py
```

from django.db import models
from django.contrib import admin
class Library_DB(models.Model):
    serial=models.IntegerField(primary_key=True);
    title=models.CharField(max_length=20);
    author=models.CharField(max_length=20);
    publishion=models.CharField(max_length=20);
    price=models.IntegerField();
class Library_DBAdmin(admin.ModelAdmin):
    list_display=("serial","title","author","price");
```
admin.py
```
from django.contrib import admin
from .models import Library_DB,Library_DBAdmin
admin.site.register(Library_DB,Library_DBAdmin)
```


## OUTPUT
![Screenshot 2024-03-05 112235](https://github.com/Suresh-2006/ORM/assets/149347611/b5ec93ce-7a23-41fe-86cf-a1e02f132eb8)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
