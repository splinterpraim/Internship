from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from .models import CustomUser, Student, Company, Resume, Vacancy, Review
from .forms import (#ProfileCustomUserFrom,
					#ProfileStudentFrom, 
					#PROFILE
					ProfileStudentChangeFullNameFrom,
					ProfileChangeUsernameFrom,
					ProfileStudentChangeDateFrom,
					ProfileStudentChangePhoneFrom,
					ProfileStudentChangeGroupFrom,
					ProfileChangeNameFrom,
					ProfileChangePhotoFrom,
					ProfileChangeDescriptionFrom,
					ProfileChangeAddressFrom,
					ProfileChangePhoneFrom,
					ProfileChangeSiteNameFrom,
					CreateResumeForm,
					#RESUME
					MyResumeChangeNameForm,
					MyResumeChangeExperienceForm,
					MyResumeChangeResponsibilitiesForm,
					MyResumeChangeAchievementsForm,
					MyResumeChangeSkillsForm,
					MyResumeChangeAboutSelfForm,
					#VACANCY
					CreateVacancyForm,
					MyVacancyChangeNameForm,
					MyVacancyChangeDescriptionForm,
					MyVacancyChangeResponsibilitiesForm,
					MyVacancyChangeRequirementsForm,
					MyVacancyChangeConditionsForm,
					MyVacancyChangeSkillsForm,
					#REVIEW
					CreateReviewForm

					)

from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from  django.http import HttpResponse
from .my_features import ProfileHelp

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseNotFound




class CustomLoginView(auth_views.LoginView):
	model = settings.AUTH_USER_MODEL


# @login_required
# def profile(request):
# 	form = ProfileCustomUserFrom()
# 	return render(request,'main_site/profile.html',{'section':'profile',
# 						  							'name':request.user.username,
# 						  							'form':form})

#@login_required
class ProfileDetailView(LoginRequiredMixin,TemplateView):
	#model = CustomUser

	template_name = 'main_site/profile.html'
	#context_object_name = 'users'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = CustomUser.objects.get(id=self.request.user.id)
		student = Student.objects.get(id=user.students.id)
		context['user'] = user
		context['forms'] = ProfileStudentFrom
		context['form'] = ProfileCustomUserFrom
		return context



###################################################### RESUME ###################

class CreateResumeView(LoginRequiredMixin,CreateView):
	
	model = Resume
	form_class = CreateResumeForm
	template_name = 'main_site/resume/create_resume.html'

	def form_valid(self, form):
		form.instance.student = self.request.user.students
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'create_resume'
		return context

class MyResumeListView(LoginRequiredMixin,ListView):
	model = Resume
	template_name = 'main_site/resume/my_resume_list.html'
	context_object_name = 'resumes'
	def get_queryset(self):
		queryset = Resume.objects.filter(student=self.request.user.students).exclude(status='blocked').order_by('-updated_by').all()
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'my_resume_list'
		return context


class MyResumeDetailView(LoginRequiredMixin,DetailView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	context_object_name = 'resume'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Resume.objects.filter(student=self.request.user.students).exclude(status='blocked').get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')
		


def my_resume_make_published(request,  pk, who):

	resume = Resume.objects.get(id=pk)
	resume.status = 'published'
	resume.save()
	if who == 1: #0 - пришел с my_resume_detail, 1 - пришел с my_resume_list
		return redirect('my_resume_list')
	else:
		return redirect('my_resume_detail',pk=pk)

def my_resume_make_closed(request,  pk):
	resume = Resume.objects.get(id=pk)
	resume.status = 'closed'
	resume.save()
	return redirect('my_resume_detail',pk=pk)

def my_resume_delete(request,  pk):
	resume = Resume.objects.get(id=pk)
	resume.delete()
	return redirect('my_resume_list')



class MyResumeChangeNameView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeNameForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["name_div"] = True
		return context


class MyResumeChangeExperienceView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeExperienceForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["experience_div"] = True
		return context


class MyResumeChangeResponsibilitiesView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeResponsibilitiesForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["responsibilities_div"] = True
		return context


class MyResumeChangeAchievementsView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeAchievementsForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["achievements_div"] = True
		return context

class MyResumeChangeSkillsView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeSkillsForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["skills_div"] = True
		return context

class MyResumeChangeAboutSelfView(LoginRequiredMixin,UpdateView):
	model = Resume
	template_name = 'main_site/resume/my_resume_detail.html'
	form_class = MyResumeChangeAboutSelfForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["about_self_div"] = True
		return context

########################################################################################

###################################################### VACANCY ###############################

class CreateVacancyView(LoginRequiredMixin,CreateView):
	
	model = Vacancy
	form_class = CreateVacancyForm
	template_name = 'main_site/vacancy/create_vacancy.html'

	def form_valid(self, form):
		form.instance.company = self.request.user.companys
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'create_vacancy'
		return context


class MyVacancyListView(LoginRequiredMixin,ListView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_list.html'
	context_object_name = 'vacancys'
	def get_queryset(self):
		queryset = Vacancy.objects.filter(company=self.request.user.companys).exclude(status='blocked').order_by('-updated_by').all()
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'my_vacancy_list'
		return context


class MyVacancyDetailView(LoginRequiredMixin,DetailView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	context_object_name = 'vacancy'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Vacancy.objects.filter(company=self.request.user.companys).exclude(status='blocked').get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')
		

def my_vacancy_make_published(request,  pk, who):

	vacancy = Vacancy.objects.get(id=pk)
	vacancy.status = 'published'
	vacancy.save()
	if who == 1: #0 - пришел с my_vacancy_detail, 1 - пришел с my_vacancy_list
		return redirect('my_vacancy_list')
	else:
		return redirect('my_vacancy_detail',pk=pk)

def my_vacancy_make_closed(request,  pk):
	vacancy = Vacancy.objects.get(id=pk)
	vacancy.status = 'closed'
	vacancy.save()
	return redirect('my_vacancy_detail',pk=pk)

def my_vacancy_delete(request,  pk):
	vacancy = Vacancy.objects.get(id=pk)
	vacancy.delete()
	return redirect('my_vacancy_list')



class MyVacancyChangeNameView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeNameForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["name_div"] = True
		return context


class MyVacancyChangeDescriptionView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeDescriptionForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["description_div"] = True
		return context


class MyVacancyChangeResponsibilitiesView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeResponsibilitiesForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["responsibilities_div"] = True
		return context


class MyVacancyChangeRequirementsView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeRequirementsForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["requirements_div"] = True
		return context


class MyVacancyChangeConditionsView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeConditionsForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["conditions_div"] = True
		return context


class MyVacancyChangeSkillsView(LoginRequiredMixin,UpdateView):
	model = Vacancy
	template_name = 'main_site/vacancy/my_vacancy_detail.html'
	form_class = MyVacancyChangeSkillsForm
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["skills_div"] = True
		return context




##########################################################################################

################################################### REVIEW ########################

class CreateReviewView(LoginRequiredMixin,CreateView):
	
	model = Review
	form_class = CreateReviewForm
	template_name = 'main_site/review/create_review.html'

	def form_valid(self, form):
		form.instance.student = self.request.user.students
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'create_review'
		return context


class MyReviewListView(LoginRequiredMixin,ListView):
	model = Review
	template_name = 'main_site/review/my_review_list.html'
	context_object_name = 'reviews'
	def get_queryset(self):
		queryset = Review.objects.filter(student=self.request.user.students).order_by('-created_by').all()
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'my_review_list'
		return context

class MyReviewDetailView(LoginRequiredMixin,DetailView):
	model = Review
	template_name = 'main_site/review/my_review_detail.html'
	context_object_name = 'review'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Review.objects.filter(student=self.request.user.students).get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')

		

############################################################################
################################################################################

####################################################### PROFILE ##################################


## STUDENT
@login_required
def profile_change_full_name(request):
	obj_profile = ProfileHelp(request)
	obj_profile.form = ProfileStudentChangeFullNameFrom
	context = {'name_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_date_of_birth(request):
	obj_profile = ProfileHelp(request)
	obj_profile.form = ProfileStudentChangeDateFrom
	context = {'date_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_group(request):
	obj_profile = ProfileHelp(request)
	obj_profile.form = ProfileStudentChangeGroupFrom
	context = {'group_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()



## COMPANY
@login_required
def profile_change_name(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'company'
	obj_profile.form = ProfileChangeNameFrom
	context = {'name_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_photo(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'company'
	obj_profile.form = ProfileChangePhotoFrom
	context = {'photo_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_description(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'company'
	obj_profile.form = ProfileChangeDescriptionFrom
	context = {'description_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_address(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'company'
	obj_profile.form = ProfileChangeAddressFrom
	context = {'address_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_site_name(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'company'
	obj_profile.form = ProfileChangeSiteNameFrom
	context = {'site_name_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()



## GENERAL
@login_required
def profile(request):
	obj_profile = ProfileHelp(request)
	return render(request, obj_profile.profile_template, obj_profile.get_context())


@login_required
def profile_change_username(request):
	obj_profile = ProfileHelp(request,user_render=True)
	obj_profile.view_role = 'both'
	obj_profile.form = ProfileChangeUsernameFrom
	context = {'username_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


@login_required
def profile_change_phone(request):
	obj_profile = ProfileHelp(request)
	obj_profile.view_role = 'both'
	if request.user.role == 'student':
		obj_profile.form = ProfileStudentChangePhoneFrom
	elif request.user.role == 'company':
		obj_profile.form = ProfileChangePhoneFrom
	context = {'phone_div': True}
	obj_profile.add_context(context)
	return obj_profile.main()


########################################################################################

####################################################################################
	# Create your views here.




# class PCN(LoginRequiredMixin,UpdateView):
# 	#model = CustomUser

# 	template_name = 'main_site/profile/profile.html'
# 	form_class = ProfileStudentChangeNameFrom
# 	success_url = 'profile'
# 	#context_object_name = 'users'

# 	def get(self, request, *args, **kwargs):
# 	    self.object = self.get_object()
# 	    return super().get(request, *args, **kwargs)
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		user = CustomUser.objects.get(id=self.request.user.id)
# 		student = Student.objects.get(id=user.students.id)
# 		context['user'] = user
# 		context['student'] = student
# 		context['form'] = ProfileStudentChangeNameFrom(instance=student)
# 		context['name_div'] = True
# 		return context

# 	def get_success_url(self):

# 		return reverse('profile_change_name', kwargs={'pk': self.request.user.students.id})