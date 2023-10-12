from django.urls import path
from . import views

app_name = 'GapsInSoftwareEngineeringEducation'
urlpatterns = [
    path('', views.gaps_home, name='gaps_home'),
    path('question1', views.question1, name='question1'),
    path('question2', views.question2, name='question2'),
    path('question3', views.question3, name='question3'),
    path('guessing_question1', views.guessing_question1, name='guessing_question1'),
    path('guessing_question2', views.guessing_question2, name='guessing_question2'),
    path('guessing_question3', views.guessing_question3, name='guessing_question3'),
    path('guessing_question_submission', views.guessing_question_submission, name='guessing_question_submission'),
    path('question1_submission', views.question1_submit, name='question1_submission'),
    path('question2_submission', views.question2_submit, name='question2_submission'),
    path('question3_submission', views.question3_submit, name='question3_submission'),
    path('resources', views.resources, name='resources'),
    path('skill_pracitce', views.skill_practice, name='skill_practice'),
]
