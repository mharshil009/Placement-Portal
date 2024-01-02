from django.db import models

# Create your models here.

class admin(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    
class clg_degree(models.Model):
    id = models.IntegerField(primary_key=True)
    degree_id = models.IntegerField()
    tpo_id = models.IntegerField()
    status = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
class clg_semester(models.Model):
    id = models.IntegerField(primary_key=True)
    semester_id = models.IntegerField()
    tpo_id = models.IntegerField()
    status = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
class company(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=10)
    company_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile_no = models.IntegerField()
    website_link = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    status = models.IntegerField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
class degree(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    status = models.IntegerField(default=False)
    update_date = models.DateTimeField(auto_now_add=True)
    
class interns(models.Model):
    id = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    companyid = models.IntegerField()
    jobid = models.IntegerField()
    reason = models.CharField(max_length=100)
    std_level = models.IntegerField()
    student_join = models.IntegerField()
    status = models.IntegerField(default=False)
    apply_date = models.DateTimeField(auto_now_add=True)

class jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    companyid = models.IntegerField()
    tpo_id = models.IntegerField()
    job_title = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    salary = models.IntegerField()
    skill = models.CharField(max_length=200)
    experience = models.IntegerField()
    no_position = models.IntegerField()
    type = models.CharField(max_length=200)
    type_of_job = models.CharField(max_length=20)
    end_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    status = models.IntegerField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
class jobslevel(models.Model):
    id = models.IntegerField(primary_key=True)
    companyid = models.IntegerField()
    job_id = models.IntegerField()
    level_type = models.CharField(max_length=10)
    level_name = models.CharField(max_length=10)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
class semester(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    status = models.IntegerField(default=False)
    update_date = models.DateTimeField(auto_now_add=True)
    
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    tpo_id = models.IntegerField()
    role = models.CharField(max_length=10)
    semester = models.IntegerField()
    branch = models.CharField(max_length=5)
    student_name = models.CharField(max_length=50)
    enrollment_no = models.IntegerField()
    cgpa = models.IntegerField()
    cpi = models.IntegerField()
    backlog = models.IntegerField()
    cv = models.CharField(max_length=250)
    marksheet = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=30)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    status = models.IntegerField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
class Support(models.Model):
    id = models.IntegerField(primary_key=True)
    companyid = models.IntegerField()
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile_no = models.IntegerField()
    message = models.TextField(max_length=500)
    reply = models.TextField(max_length=500)
    status = models.IntegerField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
class tpo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    clg_code = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    contact_no = models.IntegerField()
    password = models.CharField(max_length=30)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    status = models.IntegerField(default=False)
    crete_date = models.DateTimeField(auto_now_add=True)