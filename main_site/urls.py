from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import  redirect
urlpatterns = [
    path('',views.main_site,name='main_site'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/',views.profile , name='profile'),

    ## STUDENT
    path('profile/change-full-name/',views.profile_change_full_name , name='profile_change_full_name'),
    path('profile/change-date-of-birth/',views.profile_change_date_of_birth , name='profile_change_date_of_birth'),
    path('profile/change-phone/',views.profile_change_phone , name='profile_change_phone'),
    path('profile/change-group/',views.profile_change_group , name='profile_change_group'),

    path('search/resume/',views.ResumeListView.as_view() , name='resume_list'),

    path('resume/RESUME-<int:pk>/',views.ResumeDetailView.as_view() , name='resume_detail'),
    path('resume/RESUME-<int:pk>/make_offer/',views.CreateResponseView.as_view() , name='make_offer'),
    path('resume/create/',views.CreateResumeView.as_view() , name='create_resume'),
    path('resume/my/',views.MyResumeListView.as_view() , name='my_resume_list'),
    path('resume/my/<int:pk>/',views.MyResumeDetailView.as_view() , name='my_resume_detail'),
    path('resume/my/<int:pk>/make_published/<int:who>/',views.my_resume_make_published , name='my_resume_make_published'),
    path('resume/my/<int:pk>/make_closed/',views.my_resume_make_closed , name='my_resume_make_closed'),
    path('resume/my/<int:pk>/delete/',views.my_resume_delete , name='my_resume_delete'),
    path('resume/my/<int:pk>/change-name/',views.MyResumeChangeNameView.as_view() , name='my_resume_change_name'),
    path('resume/my/<int:pk>/change-experience/',views.MyResumeChangeExperienceView.as_view() , name='my_resume_change_experience'),
    path('resume/my/<int:pk>/change-responsibilities/',views.MyResumeChangeResponsibilitiesView.as_view() , name='my_resume_change_responsibilities'),
    path('resume/my/<int:pk>/change-achievements/',views.MyResumeChangeAchievementsView.as_view() , name='my_resume_change_achievements'),
    path('resume/my/<int:pk>/change-skills/',views.MyResumeChangeSkillsView.as_view() , name='my_resume_change_skills'),
    path('resume/my/<int:pk>/change-about-self/',views.MyResumeChangeAboutSelfView.as_view() , name='my_resume_change_about_self'),

    path('review/create/',views.CreateReviewView.as_view() , name='create_review'),
    path('review/my/',views.MyReviewListView.as_view() , name='my_review_list'),
    path('review/my/<int:pk>/',views.MyReviewDetailView.as_view() , name='my_review_detail'),

    path('student/response/',views.StudentResponseListView.as_view() , name='student_response_list'),
    path('student/response/<int:pk>',views.StudentResponseDetailView.as_view() , name='student_response_detail'),




	

    ## COMPANY
    path('profile/change-name/',views.profile_change_name , name='profile_change_name'),
    path('profile/change-photo/',views.profile_change_photo , name='profile_change_photo'),
    path('profile/change-description/',views.profile_change_description , name='profile_change_description'),
    path('profile/change-address/',views.profile_change_address , name='profile_change_address'),
    path('profile/change-site-name/',views.profile_change_site_name , name='profile_change_site_name'),

    path('search/vacancy/',views.VacancyListView.as_view() , name='vacancy_list'),

    path('vacancy/VACANCY-<int:pk>/',views.VacancyDetailView.as_view() , name='vacancy_detail'),
    path('vacancy/VACANCY-<int:pk>/student_response/',views.StudentCreateResponseView.as_view() , name='student_response'),

    path('vacancy/create/',views.CreateVacancyView.as_view() , name='create_vacancy'),
    path('vacancy/my/',views.MyVacancyListView.as_view() , name='my_vacancy_list'),
    path('vacancy/my/<int:pk>/',views.MyVacancyDetailView.as_view() , name='my_vacancy_detail'),
   	path('vacancy/my/<int:pk>/make_published/<int:who>/',views.my_vacancy_make_published , name='my_vacancy_make_published'),
    path('vacancy/my/<int:pk>/make_closed/',views.my_vacancy_make_closed , name='my_vacancy_make_closed'),
    path('vacancy/my/<int:pk>/delete/',views.my_vacancy_delete , name='my_vacancy_delete'),
    path('vacancy/my/<int:pk>/change-name/',views.MyVacancyChangeNameView.as_view() , name='my_vacancy_change_name'),
    path('vacancy/my/<int:pk>/change-description/',views.MyVacancyChangeDescriptionView.as_view() , name='my_vacancy_change_description'),
    path('vacancy/my/<int:pk>/change-responsibilities/',views.MyVacancyChangeResponsibilitiesView.as_view() , name='my_vacancy_change_responsibilities'),
    path('vacancy/my/<int:pk>/change-requirements/',views.MyVacancyChangeRequirementsView.as_view() , name='my_vacancy_change_requirements'),
    path('vacancy/my/<int:pk>/change-conditions/',views.MyVacancyChangeConditionsView.as_view() , name='my_vacancy_change_conditions'),
    path('vacancy/my/<int:pk>/change-skills/',views.MyVacancyChangeSkillsView.as_view() , name='my_vacancy_change_skills'),
    
    path('company/response/',views.CompanyResponseListView.as_view() , name='company_response_list'),
    path('company/response/<int:pk>',views.CompanyResponseDetailView.as_view() , name='company_response_detail'),

    path('company/response/<int:pk>/make_offer',views.company_make_offer , name='company_make_offer'),
    path('company/response/<int:pk>/make_reject',views.company_make_reject , name='company_make_reject'),
    path('company/response/<int:pk>/make_offer_completed',views.company_make_offer_completed , name='company_make_offer_completed'),

   	## GENERAL
    path('profile/change-username/',views.profile_change_username, name='profile_change_username'),
    path('document_list/',views.DocumentListView.as_view(), name='document_list'),

    path('profile_change_photo_new/',views.profile_change_photo_new, name='profile_change_photo_new'),



]
#profile_change_username 
#profile_change_name