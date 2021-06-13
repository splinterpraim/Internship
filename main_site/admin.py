from django.contrib import admin
from .models import Student, Company, Review, Vacancy, Resume, Response, Skill, Document, CustomUser
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('role',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	#add_from = CustomUserCreationForm
	#form = CustomUserChangeForm
	#model = CustomUser
	list_display = ['username','role','student_link','company_link']
	list_display_links = ['username','student_link','company_link']
	list_filter = ('role',)
	search_fields = ['username','students__name','company__name']
	ordering = ['username']

	add_fieldsets = (
        (None, {
            'fields': ('username', 'role', 'password1', 'password2')}
         ),
    )
	fieldsets =(
        (None, {
            'fields': ('username', 'role','is_active','is_staff','is_superuser','date_joined','last_login')}
         ),
    )

    

	#exclude = ('group','user_permissions','first_name','last_name')
	list_per_page = 20
	def student_link(self,obj):
		if obj.role == 'student':
			url = reverse('admin:main_site_student_change', args=(obj.students.id,))
			name_url = obj.students.__str__()
			if obj.students.name == '':
				name_url = obj.username
			return format_html("<a href='{}'>{}</a>",url,name_url)
		elif obj.role == 'company':
			return format_html("<a href='{}'>{}</a>",'','')
	student_link.short_description = 'Профиль Студента'

	def company_link(self,obj):
		if obj.role == 'company':
			url = reverse('admin:main_site_company_change', args=(obj.companys.id,))
			name_url = obj.companys.name
			if obj.companys.name == '':
				name_url = obj.username
			return format_html("<a href='{}'>{}</a>",url,name_url)
		elif obj.role == 'student':
			return format_html("<a href='{}'>{}</a>",'','')
	company_link.short_description = 'Профиль Компании'

#admin.site.register(CustomUser,CustomUserAdmin)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	search_fields = ['id','name','last_name','father_name']
	list_display_links = ['id','__str__','user_link']
	list_filter = ('university_group',)
	list_display = ['id','__str__','user_link','university_group','phone']
	list_per_page = 20
	#ordering = ('-user__created',)
	def user_link(self,obj):
		url = reverse('admin:main_site_customuser_change', args=(obj.user.id,))
		name_url = obj.user.__str__()
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	user_link.short_description = 'Пользователь'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	search_fields = ['id','name',]
	list_display_links = ['id','name','user_link','site_link']
	#list_filter = ('mark',)
	list_display = ['id','name','user_link','site_link','address']
	list_per_page = 20
	#ordering = ('-user__created',)

	def user_link(self,obj):
		url = reverse('admin:main_site_customuser_change', args=(obj.user.id,))
		name_url = obj.user.__str__()
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	user_link.short_description = 'Пользователь'

	def site_link(self,obj):
		url = f'http://{obj.site_name}/'
		name_url = obj.site_name
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	site_link.short_description = 'Сайт'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	search_fields = ['id','student__id','student__name','student__user__username','company__name']
	list_filter = ('mark',)
	list_display = ['id','company_link','student_link','mark']
	list_display_links = ['id','company_link','student_link']
	list_per_page = 20
	ordering = ('-created_by',)

	def student_link(self,obj):
		url = reverse('admin:main_site_student_change', args=(obj.student.id,))
		name_url = obj.student
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	student_link.short_description = 'Студент'

	def company_link(self,obj):
		url = reverse('admin:main_site_company_change', args=(obj.company.id,))
		name_url = obj.company
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	company_link.short_description = 'Компания'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
	search_fields = ['name','company__name','skills__name']
	list_filter = ('status','skills__name')
	list_display = ['id','name','company_link','status']
	list_display_links = ['id','name','company_link']
	list_per_page = 20
	ordering = ('-updated_by',)

	def company_link(self,obj):
		url = reverse('admin:main_site_company_change', args=(obj.company.id,))
		name_url = obj.company
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	company_link.short_description = 'Компания'


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
	search_fields = ['name','student__name','student__last_name','student__father_name','skills__name']
	list_filter = ('status','skills__name')
	list_display = ['id','name','student_link','status']
	list_display_links = ['id','name','student_link']
	list_per_page = 20
	ordering = ('-updated_by',)

	def student_link(self,obj):
		url = reverse('admin:main_site_student_change', args=(obj.student.id,))
		name_url = obj.student
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	student_link.short_description = 'Студент'


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
	search_fields = ['vacancy__name','resume__name']
	list_filter = ('status',)
	list_display = ['id','vacancy_link','resume_link','status']
	list_display_links = ['id','vacancy_link', 'resume_link']
	list_per_page = 20
	ordering = ('-updated_by',)

	def vacancy_link(self,obj):
		url = reverse('admin:main_site_vacancy_change', args=(obj.vacancy.id,))
		name_url = obj.vacancy
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	vacancy_link.short_description = 'Вакансия'


	def resume_link(self,obj):
		url = reverse('admin:main_site_resume_change', args=(obj.resume.id,))
		name_url = obj.resume
		return format_html("<a href='{}'>{}</a>",url,name_url)
		
	resume_link.short_description = 'Резюме'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	search_fields = ['name',]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	search_fields = ['name',]

# Register your models here.
