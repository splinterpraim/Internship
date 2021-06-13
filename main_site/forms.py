from django.forms import models
from django.forms import (ModelForm,
						  TextInput, 
						  Textarea,
						  Select,
						  SelectMultiple, 
						  RadioSelect, CheckboxSelectMultiple, Select, CheckboxInput,)

from .models import CustomUser, Student, Company, Resume, Vacancy,  Review

# class ProfileCustomUserFrom(models.ModelForm):
	
# 	class Meta:
# 		model = CustomUser
# 		fields = ('username',)

# class ProfileStudentFrom(models.ModelForm):
# 	class Meta:
# 		model = Student
# 		fields = ("name",)

# class ProfileCompanyFrom(models.ModelForm):
# 	class Meta:
# 		model = Company
# 		fields = ("name",)

# student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='resumes', verbose_name="Студент")
# 	skills = models.ManyToManyField(Skill,related_name='resumes', verbose_name="Навыки")
# 	name = models.CharField('Название',max_length=100)
# 	experience = models.TextField('Опыт')
# 	responsibilities = models.TextField('Обязанности') #обязанности
# 	achievements = models.TextField('Достижения') #достижения
# 	about_self = models.TextField('О себе')
# 	created_by = models.DateTimeField(auto_now_add=True)
# 	updated_by =  models.DateTimeField(auto_now=True)
# 	status = mod

################################################## RESUME #############################

class CreateResumeForm(ModelForm):
	class Meta:
		model = Resume
		exclude = ('student','status')
		fields = ['name','experience','responsibilities','achievements','skills','about_self']
		widgets = {
			'name': TextInput(attrs={'placeholder': 'название резюме','style':'background-color: white;'}),
			'experience': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваш опыт работы','style':'background-color: white;'}),
			'responsibilities': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваши обязанности','style':'background-color: white;'}),
			'achievements': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваши достижения','style':'background-color: white;'}),
			'about_self': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'дополните информацию о себе','style':'background-color: white;'}),
			}
		help_texts = {
			'name': 'Дайте осмысленное название полю',
			'skills':'Выберите навыки которыми обладаете'
		}

class MyResumeChangeNameForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['name',]

class MyResumeChangeExperienceForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['experience',]

class MyResumeChangeResponsibilitiesForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['responsibilities',]

class MyResumeChangeAchievementsForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['achievements',]

class MyResumeChangeSkillsForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['skills',]

class MyResumeChangeAboutSelfForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['about_self',]

################################################ VACANCY ####################

class CreateVacancyForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['name','description','responsibilities','requirements','conditions','skills']
		widgets = {
			'name': TextInput(attrs={'placeholder': 'название резюме','style':'background-color: white;'}),
			'description': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваш опыт работы','style':'background-color: white;'}),
			'responsibilities': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваши обязанности','style':'background-color: white;'}),
			'requirements': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваши достижения','style':'background-color: white;'}),
			'conditions': Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'дополните информацию о себе','style':'background-color: white;'}),
			}
		help_texts = {
			'name': 'Дайте осмысленное название полю',
			'skills':'Выберите навыки которыми обладаете'
		}



class MyVacancyChangeNameForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['name',]

class MyVacancyChangeDescriptionForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['description',]

class MyVacancyChangeResponsibilitiesForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['responsibilities',]

class MyVacancyChangeRequirementsForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['requirements',]

class MyVacancyChangeConditionsForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['conditions',]

class MyVacancyChangeSkillsForm(ModelForm):
	class Meta:
		model = Vacancy
		fields = ['skills',]
	

#######################################################################################

############################################### REVIEW ###########################


class CreateReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['company','mark','text']
		widgets = {
		# 	'company': TextInput(attrs={'placeholder': 'название резюме','style':'background-color: white;'}),
			# 'mark': RadioSelect(attrs={'style':'list-style-type: none;'}),#attrs={'cols': 50, 'rows': 5, 'placeholder': 'ваш опыт работы','style':'background-color: white;'}),
			'text': Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'Текст вашего отзыва','style':'background-color: white;'}),
			}
		help_texts = {
			'company': 'Выберите компанию',
			'mark':'Поставте справедливую оценку',
			
		}

		

	

#############################################################################

##################################################### PROFILE ######################

## STUDENT
class ProfileStudentChangeFullNameFrom(ModelForm):
	class Meta:
		model = Student
		fields = ('name','last_name','father_name')
	def get_func_name(self):
		return 'save_full_name'

	
class ProfileStudentChangeDateFrom(ModelForm):
	class Meta:
		model = Student
		fields = ('date_of_birth',)
	def get_func_name(self):
		return 'save_date_of_birth'

class ProfileStudentChangePhoneFrom(ModelForm):
	class Meta:
		model = Student
		fields = ('phone',)
	def get_func_name(self):
		return 'save_phone'


class ProfileStudentChangeGroupFrom(ModelForm):
	class Meta:
		model = Student
		fields = ('university_group',)
	def get_func_name(self):
		return 'save_group'


## COMPANY
class ProfileChangeNameFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('name',)
	def get_func_name(self):
		return 'save_name'

class ProfileChangePhotoFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('photo',)
	def get_func_name(self):
		return 'save_photo'

class ProfileChangeDescriptionFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('description',)
	def get_func_name(self):
		return 'save_description'

class ProfileChangeAddressFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('address',)
	def get_func_name(self):
		return 'save_address'

class ProfileChangePhoneFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('phone',)
	def get_func_name(self):
		return 'save_phone'

class ProfileChangeSiteNameFrom(ModelForm):
	class Meta:
		model = Company
		fields = ('site_name',)
	def get_func_name(self):
		return 'save_site_name'


## GENERAL
class ProfileChangeUsernameFrom(ModelForm):
	class Meta:
		model = CustomUser
		fields = ('username',)
	def get_func_name(self):
		return 'save_username'




####################################################################
	# def get_initial_for_field(self, field, field_name):
	# 	if field_name == 'name':
	# 		return self.instance.name
        # else:
        #     return super(ItemForm, self).get_initial_for_field(field, field_name)

