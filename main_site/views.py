from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from .models import CustomUser, Student, Company, Resume, Vacancy, Review, Response, Document
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
					CreateReviewForm,
					#RESPONSE
					CreateResponseForm,
					StudentCreateResponseForm

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
from django.db.models import Q 



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


@login_required
def main_site(request):
	return redirect('profile')

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
		

@login_required
def my_resume_make_published(request,  pk, who):

	resume = Resume.objects.get(id=pk)
	resume.status = 'published'
	resume.save()
	if who == 1: #0 - пришел с my_resume_detail, 1 - пришел с my_resume_list
		return redirect('my_resume_list')
	else:
		return redirect('my_resume_detail',pk=pk)

@login_required
def my_resume_make_closed(request,  pk):
	resume = Resume.objects.get(id=pk)
	resume.status = 'closed'
	resume.save()
	return redirect('my_resume_detail',pk=pk)

@login_required
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
		
@login_required
def my_vacancy_make_published(request,  pk, who):

	vacancy = Vacancy.objects.get(id=pk)
	vacancy.status = 'published'
	vacancy.save()
	if who == 1: #0 - пришел с my_vacancy_detail, 1 - пришел с my_vacancy_list
		return redirect('my_vacancy_list')
	else:
		return redirect('my_vacancy_detail',pk=pk)

@login_required
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
def profile_change_photo_new(request):
	if request.method == "POST":
		form = ProfileChangePhotoFrom(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("success")
	else:
		form = ProfileChangePhotoFrom()
	p = Company.objects.last()
	return render(request, "main_site/profile/profile_change_username.html", {"form": form, "p": p})


def success(request):
    return HttpResponse("Successfully uploaded")


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


###############################################################################################

################################################### SEARCH #################################



class ResumeListView(LoginRequiredMixin,ListView):
	model = Resume
	template_name = 'main_site/resume/resume_list.html'
	context_object_name = 'resumes'

	def get_queryset(self):
		queryset = Resume.objects.filter(status='published',).order_by('-updated_by').all()
		query = self.request.GET.get('search')
		if query:
			queryset = Resume.objects.filter(status='published',).filter(Q(name__icontains=query) | Q(skills__name__icontains=query)).distinct().order_by('-updated_by').all()
		if not self.request.GET.get('filter_clance'):
			filter_data = self.request.GET.get('filter')
			if filter_data:
				queryset = queryset.order_by(filter_data)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'resume_list'
		search_value = self.request.GET.get('search')
		if not search_value:
			search_value = ''
		context['search_value'] = search_value 
		context['filter'] = self.request.GET.get('filter')
		return context

class ResumeDetailView(LoginRequiredMixin,DetailView):
	model = Resume
	template_name = 'main_site/resume/resume_detail.html'
	context_object_name = 'resume'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Resume.objects.filter(status='published').get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		responses = dict()
		responses['offer'] = Response.objects.filter(vacancy__company=self.request.user.companys).filter(resume__id=self.kwargs.get('pk')).filter(status='offer')
		responses['student_response'] = Response.objects.filter(vacancy__company=self.request.user.companys).filter(resume__id=self.kwargs.get('pk')).filter(status='student_response')
		responses['reject'] = Response.objects.filter(vacancy__company=self.request.user.companys).filter(resume__id=self.kwargs.get('pk')).filter(status='reject')
		responses['offer_completed'] = Response.objects.filter(vacancy__company=self.request.user.companys).filter(resume__id=self.kwargs.get('pk')).filter(status='offer_completed')
		context["responses"] = responses
		return context


class VacancyListView(LoginRequiredMixin,ListView):
	model = Vacancy
	template_name = 'main_site/vacancy/vacancy_list.html'
	context_object_name = 'vacancys'

	def get_queryset(self):
		queryset = Vacancy.objects.filter(status='published',).order_by('-updated_by').all()
		query = self.request.GET.get('search')
		if query:
			queryset = Vacancy.objects.filter(status='published',).filter(Q(name__icontains=query) | Q(skills__name__icontains=query)).distinct().order_by('-updated_by').all()
		if not self.request.GET.get('filter_clance'):
			filter_data = self.request.GET.get('filter')
			if filter_data:
				queryset = queryset.order_by(filter_data)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'vacancy_list'
		search_value = self.request.GET.get('search')
		if not search_value:
			search_value = ''
		context['search_value'] = search_value 
		context['filter'] = self.request.GET.get('filter')
		return context

class VacancyDetailView(LoginRequiredMixin,DetailView):
	model = Vacancy
	template_name = 'main_site/vacancy/vacancy_detail.html'
	context_object_name = 'vacancy'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Vacancy.objects.filter(status='published').get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		responses = dict()
		responses['offer'] = Response.objects.filter(resume__student=self.request.user.students).filter(vacancy__id=self.kwargs.get('pk')).filter(status='offer')
		responses['student_response'] = Response.objects.filter(resume__student=self.request.user.students).filter(vacancy__id=self.kwargs.get('pk')).filter(status='student_response')
		responses['reject'] = Response.objects.filter(resume__student=self.request.user.students).filter(vacancy__id=self.kwargs.get('pk')).filter(status='reject')
		responses['offer_completed'] = Response.objects.filter(resume__student=self.request.user.students).filter(vacancy__id=self.kwargs.get('pk')).filter(status='offer_completed')
		context["responses"] = responses
		return context


################################################### Response ##############################

class CreateResponseView(LoginRequiredMixin,CreateView):
	
	model = Response
	form_class = CreateResponseForm
	template_name = 'main_site/response/create_response.html'
	empty_field_vacancy = False

	def form_valid(self, form):

		form.instance.resume = Resume.objects.get(id=self.kwargs.get('pk'))  
		form.instance.status = 'offer'
		return super().form_valid(form)

	def get_company(self):
		return self.request.user.companys

	
	def get_form(self, *args, **kwargs):
		form = super(CreateResponseView, self).get_form(*args, **kwargs)
		form.fields['vacancy'].queryset = Vacancy.objects.filter(company=self.get_company()).filter(status='published').exclude(responses__resume__id=self.kwargs.get('pk'))
		if not form.fields['vacancy'].queryset:
			self.empty_field_vacancy = True
		return form

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'create_response'
		context["resume"] = Resume.objects.get(id=self.kwargs.get('pk')) 
		if self.empty_field_vacancy:
			context["empty_field_vacancy"] = self.empty_field_vacancy
		return context



class CompanyResponseListView(LoginRequiredMixin,ListView):
	model = Response
	template_name = 'main_site/response/company_response_list.html'
	context_object_name = 'responses'
	ordering = ['status']
	def get_queryset(self):
		
		ordering = self.request.GET.get('filter')
		if not ordering:
			ordering = 'updated_by'
		queryset = Response.objects.filter(vacancy__company=self.request.user.companys).order_by(ordering)
		return queryset

	def get_ordering(self):
		ordering = self.request.GET.get('filter')
		print("d")
		return ordering

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'company_response_list'
		context["filter"] = self.request.GET.get('filter')

		return context


class CompanyResponseDetailView(LoginRequiredMixin,DetailView):
	model = Response
	template_name = 'main_site/response/company_response_detail.html'
	context_object_name = 'response'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Response.objects.filter(vacancy__company=self.request.user.companys).get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')



@login_required
def company_make_offer(request, pk): 
	response = Response.objects.get(id=pk)
	response.status = 'offer'
	response.save()
	return redirect('company_response_detail', pk=pk)

@login_required
def company_make_reject(request, pk):
	response = Response.objects.get(id=pk)
	response.status = 'reject'
	response.save()
	return redirect('company_response_detail', pk=pk)

@login_required
def company_make_offer_completed(request, pk):
	response = Response.objects.get(id=pk)
	response.status = 'offer_completed'
	response.save()
	return redirect('company_response_detail', pk=pk)


class StudentCreateResponseView(LoginRequiredMixin,CreateView):
	
	model = Response
	form_class = StudentCreateResponseForm
	template_name = 'main_site/response/student_response.html'
	empty_field_resume = False

	def form_valid(self, form):
		form.instance.vacancy = Vacancy.objects.get(id=self.kwargs.get('pk'))  
		form.instance.status = 'student_response'
		return super().form_valid(form)

	def get_student(self):
		return self.request.user.students

	def get_form(self, *args, **kwargs):
		form = super(StudentCreateResponseView, self).get_form(*args, **kwargs)
		form.fields['resume'].queryset = Resume.objects.filter(student=self.get_student()).filter(status='published').exclude(responses__vacancy__id=self.kwargs.get('pk'))
		if not form.fields['resume'].queryset:
			self.empty_field_resume = True
		return form

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'student_response'
		context["vacancy"] = Vacancy.objects.get(id=self.kwargs.get('pk')) 
		if self.empty_field_resume:
			context["empty_field_resume"] = self.empty_field_resume
		return context


class StudentResponseListView(LoginRequiredMixin,ListView):
	model = Response
	template_name = 'main_site/response/student_response_list.html'
	context_object_name = 'responses'
	ordering = ['status']

	def get_queryset(self):
		ordering = self.request.GET.get('filter')
		if not ordering:
			ordering = '-updated_by'
		queryset = Response.objects.filter(resume__student=self.request.user.students).order_by(ordering)
		return queryset
# вроде не нужно
	def get_ordering(self):
		ordering = self.request.GET.get('filter')
		return ordering

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["section"] = 'student_response_list'
		context["filter"] = self.request.GET.get('filter')

		return context


class StudentResponseDetailView(LoginRequiredMixin,DetailView):
	model = Response
	template_name = 'main_site/response/student_response_detail.html'
	context_object_name = 'response'

	def get_object(self, queryset=None):
		pk = self.kwargs.get('pk')
		try:
			return Response.objects.filter(resume__student=self.request.user.students).get(id=pk)
		except ObjectDoesNotExist:
			raise Http404('Ох, нет объекта;)')


################################### DOCUMENT ###########################

class DocumentListView(LoginRequiredMixin,ListView):
	model = Document
	template_name = 'main_site/document_list.html'
	context_object_name = 'documents'






##############################################################
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