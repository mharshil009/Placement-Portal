from django.urls import path
from .views import AdminAV, AdminDetailAV, clgDegreeAV, clgdegreedetailAV, clg_semesterAV, clg_semesterdetailAV, companyAV, companydetailAV, degreeAV, degreedetailAV, internsAV, internsdetailAV, jobsAV, jobsdetailAV, jobslevelAV,jobsleveldetailAV, semesterAV, semesterdetailAV, studentAV, studentdetailAV, SupportAV, SupportdetailAV, tpoAV, tpodetailAV

urlpatterns = [
    path('admin/', AdminAV.as_view(), name='adminview'),
    path('admin/<int:pk>', AdminDetailAV.as_view(), name='adminview'),
    path('clgdegree/', clgDegreeAV.as_view(), name='clgdegree'),
    path('clgdegree/<int:pk>', clgdegreedetailAV.as_view(), name='clgdegree'),
    path('clgsemester/', clg_semesterAV.as_view(), name='clgsemester'),
    path('clgsemester/<int:pk>', clg_semesterdetailAV.as_view(), name='clgdegree'),
    path('company/', companyAV.as_view(), name='company'),
    path('company/<int:pk>', companydetailAV.as_view(), name='clgdegree'),
    path('degree/', degreeAV.as_view(), name='degree'),
    path('degree/<int:pk>', degreedetailAV.as_view(), name='degree'),
    path('interns/', internsAV.as_view(), name='interns'),
    path('interns/<int:pk>', internsdetailAV.as_view(), name='interns'),
    path('jobs/', jobsAV.as_view(), name='jobs'),
    path('jobs/<int:pk>', jobsdetailAV.as_view(), name='jobs'),
    path('jobslevel/', jobslevelAV.as_view(), name='jobslevel'),
    path('jobslevel/<int:pk>', jobsleveldetailAV.as_view(), name='jobslevel'),
    path('semester/', semesterAV.as_view(), name='semester'),
    path('semester/<int:pk>', semesterdetailAV.as_view(), name='semester'),
    path('student/', studentAV.as_view(), name='student'),
    path('student/<int:pk>', studentdetailAV.as_view(), name='student'),
    path('support/', SupportAV.as_view(), name='support'),
    path('support/<int:pk>', SupportdetailAV.as_view(), name='support'),
    path('tpo/', tpoAV.as_view(), name='tpo'),
    path('tpo/<int:pk>', tpodetailAV.as_view(), name='tpodetail'),
]
