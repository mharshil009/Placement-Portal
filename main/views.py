from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import AdminSerializer, clg_degreeSerializer, clg_semesterSerializer, companySerializer, degreeSerializer, internsSerializer, jobsSerializer, jobslevelSerializer, SemesterSerializer, StudentSerializer, SupportSerializer, tpoSerializer
from . models import admin, clg_degree, clg_semester, company, degree, interns, jobs, jobslevel, semester, Student, Support, tpo
from rest_framework import status

# Create your views here.

# class StreamPlatformAV(APIView):
    
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True)
#         return Response(serializer.data) 

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
            
        
class AdminAV(APIView):
    
    def get(self, request):
        adminview = admin.objects.all()
        serializer = AdminSerializer(adminview, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class AdminDetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            adminview = admin.objects.get(pk=pk)
        except admin.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        adminview = AdminSerializer(adminview)
        return Response(adminview.data)
    
    def put(self, request, pk):
        adminview = admin.objects.get(pk=pk)
        serializer = AdminSerializer(adminview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        adminview = admin.objects.get(pk=pk)
        adminview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class clgDegreeAV(APIView):
        
    def get(self, request):
        clg = clg_degree.objects.all()
        serializer = clg_degreeSerializer(clg, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = clg_degreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class clgdegreedetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            adminview = clg_degree.objects.get(pk=pk)
        except admin.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        adminview = clg_degreeSerializer(adminview)
        return Response(adminview.data)
    
    def put(self, request, pk):
        adminview = clg_degree.objects.get(pk=pk)
        serializer = clg_degreeSerializer(adminview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        adminview = clg_degree.objects.get(pk=pk)
        adminview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class clg_semesterAV(APIView):
        
    def get(self, request):
        clg = clg_semester.objects.all()
        serializer = clg_semesterSerializer(clg, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = clg_semesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class clg_semesterdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            adminview = clg_semester.objects.get(pk=pk)
        except admin.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        adminview = clg_semesterSerializer(adminview)
        return Response(adminview.data)
    
    def put(self, request, pk):
        adminview = clg_semester.objects.get(pk=pk)
        serializer = clg_degreeSerializer(adminview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        adminview = clg_semester.objects.get(pk=pk)
        adminview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class companyAV(APIView):
    
    def get(self, request):
        companyobj = company.objects.all()
        serializer = companySerializer(companyobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = companySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
    
class companydetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            companyobj = company.objects.get(pk=pk)
        except admin.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        companyobj = companySerializer(companyobj)
        return Response(companyobj.data)
    
    def put(self, request, pk):
        companyobj = company.objects.get(pk=pk)
        serializer = companySerializer(companyobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        companyobj = company.objects.get(pk=pk)
        companyobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
class degreeAV(APIView):
    
    def get(self, request):
        degreeobj = degree.objects.all()
        serializer = degreeSerializer(degreeobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = degreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)

class degreedetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            degreeobj = degree.objects.get(pk=pk)
        except admin.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        degreeobj = degreeSerializer(degreeobj)
        return Response(degreeobj.data)
    
    def put(self, request, pk):
        degreeobj = degree.objects.get(pk=pk)
        serializer = degreeSerializer(degreeobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        degreeobj = degree.objects.get(pk=pk)
        degreeobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          
    
class internsAV(APIView):
    
    def get(self, request):
        internsobj = interns.objects.all()
        serializer = internsSerializer(internsobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = internsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)

class internsdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            internsobj = interns.objects.get(pk=pk)
        except interns.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        internsobj = internsSerializer(internsobj)
        return Response(internsobj.data)
    
    def put(self, request, pk):
        internsobj = interns.objects.get(pk=pk)
        serializer = internsSerializer(internsobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        internsobj = interns.objects.get(pk=pk)
        internsobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class jobsAV(APIView):
    
    def get(self, request):
        jobsobj = jobs.objects.all()
        serializer = jobsSerializer(jobsobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =jobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class jobsdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            jobsobj = jobs.objects.get(pk=pk)
        except jobs.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        jobsobj = jobsSerializer(jobsobj)
        return Response(jobsobj.data)
    
    def put(self, request, pk):
        jobsobj = jobs.objects.get(pk=pk)
        serializer = jobsSerializer(jobsobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        jobsobj = jobs.objects.get(pk=pk)
        jobsobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class jobslevelAV(APIView):
    
    def get(self, request):
        jobslevelobj = jobslevel.objects.all()
        serializer = jobslevelSerializer(jobslevelobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =jobslevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class jobsleveldetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            jobslevelobj = jobslevel.objects.get(pk=pk)
        except jobslevel.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        jobslevelobj = jobslevelSerializer(jobslevelobj)
        return Response(jobslevelobj.data)
    
    def put(self, request, pk):
        jobslevelobj = jobslevel.objects.get(pk=pk)
        serializer = jobslevelSerializer(jobslevelobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        jobslevelobj = jobslevel.objects.get(pk=pk)
        jobslevelobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class semesterAV(APIView):
    
    def get(self, request):
        semesterobj = semester.objects.all()
        serializer = SemesterSerializer(semesterobj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)    
        
class semesterdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            semesterobj = semester.objects.get(pk=pk)
        except semester.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        semesterobj = SemesterSerializer(semesterobj)
        return Response(semesterobj.data)
    
    def put(self, request, pk):
        semesterobj = semester.objects.get(pk=pk)
        serializer = SemesterSerializer(semesterobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        semesterobj = semester.objects.get(pk=pk)
        semesterobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class studentAV(APIView):
    
    def get(self, request):
        studentobj = Student.objects.all()
        serializer = StudentSerializer(studentobj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class studentdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            studentobj = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        studentobj = StudentSerializer(studentobj)
        return Response(studentobj.data)
    
    def put(self, request, pk):
        studentobj = Student.objects.get(pk=pk) 
        serializer = StudentSerializer(studentobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        studentobj = Student.objects.get(pk=pk)
        studentobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SupportAV(APIView):
    
    def get(self, request):
        supportobj = Support.objects.all()
        serializer = SupportSerializer(supportobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SupportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.errors)
        
class SupportdetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            supportobj = Support.objects.get(pk=pk)
        except Support.DoesNotExist:   
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        supportobj = SupportSerializer(supportobj)
        return Response(supportobj.data)
    
    def put(self, request, pk):
    
        supportobj = Support.objects.get(pk=pk)
        serializer = SupportSerializer(supportobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        supportobj = Support.objects.get(pk=pk)
        supportobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class tpoAV(APIView):
    
    def get(self, request):
        tpoobj = tpo.objects.all()
        serializer = tpoSerializer(tpoobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = tpoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class tpodetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            tpoobj = tpo.objects.get(pk=pk)
        except tpo.DoesNotExist:   
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        tpoobj = tpoSerializer(tpoobj)
        return Response(tpoobj.data)
    
    def put(self, request, pk):
    
        tpoobj = tpo.objects.get(pk=pk)
        serializer = tpoSerializer(tpoobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        tpoobj = tpo.objects.get(pk=pk)
        tpoobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
