from rest_framework import serializers
from . models import admin, clg_degree, clg_semester, company, degree, interns, jobs, jobslevel, semester, Student, Support, tpo

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = admin
        fields = "__all__"

class clg_degreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = clg_degree
        fields = "__all__"

class clg_semesterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = clg_semester
        fields = "__all__"
        
class companySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = company
        fields = "__all__"
        
class degreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = degree
        fields = "__all__"
        
class internsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = interns
        fields = "__all__"
        
class jobsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobs
        fields = "__all__"
    
class jobslevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = jobslevel
        fields = "__all__"
    
class SemesterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = semester
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = "__all__"
        
class SupportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Support
        fields = "__all__"

class tpoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tpo
        fields = "__all__"
        