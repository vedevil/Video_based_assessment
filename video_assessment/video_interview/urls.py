# video_interview/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('home/org/<str:org_id>/assessments/', views.assessments_for_org, name='assessments_for_org'),
    path('delete_assessment/<str:org_id>/<int:access_id>/', views.delete_assessment, name='delete_assessment'),
    path('update_assessment/<str:org_id>/<str:access_id>/', views.update_assessment, name='update_assessment'),
]
