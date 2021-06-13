from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class CustomUser(AbstractUser):
	TYPE_OF_ROLE =(
			('student','Студент'),
			('company','Компания'),
			('admin','Админ')
		)
	role = models.CharField('Роль',max_length=50, choices=TYPE_OF_ROLE,default='student')
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Skill(models.Model):
	name = models.CharField('Название',max_length=100,unique=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Навык'
		verbose_name_plural = 'Навыки'

	
class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='students', verbose_name='Пользователь')
	name = models.CharField('Имя',max_length=100)
	last_name = models.CharField('Фамилия',max_length=100)
	father_name = models.CharField('Отчество',max_length=100,blank=True)
	date_of_birth = models.DateField('Дата рождения',null=True,blank=True)
	phone = models.CharField('Телефон',max_length=12)
	university_group = models.CharField('Группа в вузе',max_length=20)

	# def get_absolute_url(self):
	# 	return reverse('profile')
	#mail, login, password, date_create,

	def __str__(self):
		return f'{self.last_name} {self.name} {self.father_name}'

	def full_name(self):
		return f'{self.last_name} {self.name} {self.father_name}'
	class Meta:
		verbose_name = 'Профиль Студента'
		verbose_name_plural = 'Профили Студентов'



class Company(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='companys', verbose_name='Пользователь')
	name = models.CharField('Название',max_length=200)
	address = models.CharField('Адрес',max_length=200)
	description = models.TextField('Описание')
	photo = models.ImageField('Фото',blank=True)#upload_to
	phone = models.CharField('Телефон',max_length=12, default=' ')
	site_name = models.CharField('Сайт',max_length=200)
	#mail, login, password, date_create,

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Профиль Компании'
		verbose_name_plural = 'Профили Компаний'


class Review(models.Model):
	MARKS_COICES = (
			('excellent','Отлично'),
			('good','Хорошо'),
			('normal','Нормально'),
			('bad','Плохо'),
		)
	student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='reviews', verbose_name="Студент")
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='reviews', verbose_name="Компания")
	mark = models.CharField('Оценка',max_length=10,choices=MARKS_COICES, default='good')
	text = models.TextField('Текст')
	created_by = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.company} ({self.student})'

	def get_absolute_url(self): 
		return reverse('my_review_detail',args=[str(self.id)]) 

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'


class Vacancy(models.Model):
	STATUS_CHOICES = (
			('blocked','Заблокированая'),
			('closed','Закрытая'),
			('published','Опубликованная'),
		)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='vacancys', verbose_name="Компания")
	skills = models.ManyToManyField(Skill, related_name='vacancys',verbose_name="Навыки")
	name = models.CharField('Название',max_length=100)
	description = models.TextField('Описание')
	responsibilities = models.TextField('Обязанности') #обязанности
	requirements = models.TextField('Требования') #требования
	conditions = models.TextField('Условия') #условия
	created_by = models.DateTimeField(auto_now_add=True)
	updated_by =  models.DateTimeField(auto_now=True)
	status = models.CharField('Статус',max_length=10,choices=STATUS_CHOICES, default='published')

	def __str__(self):
		return f'{self.name} ({self.company})'

	def get_absolute_url(self): 
		return reverse('my_vacancy_detail', args=[str(self.id)]) 

	class Meta:
		verbose_name = 'Вакансия'
		verbose_name_plural = 'Вакансии'




class Resume(models.Model):
	STATUS_CHOICES = (
			('blocked','Заблокированое'),
			('closed','Закрытое'),
			('published','Опубликованное'),
		)
	student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='resumes', verbose_name="Студент")
	skills = models.ManyToManyField(Skill,related_name='resumes', verbose_name="Навыки", blank=True)
	name = models.CharField('Название',max_length=100)
	experience = models.TextField('Опыт')
	responsibilities = models.TextField('Обязанности') #обязанности
	achievements = models.TextField('Достижения') #достижения
	about_self = models.TextField('О себе')
	created_by = models.DateTimeField(auto_now_add=True)
	updated_by =  models.DateTimeField(auto_now=True)
	status = models.CharField('Статус',max_length=20,choices=STATUS_CHOICES, default='published')

	def __str__(self):
		return f'{self.name} ({self.student})'

	def get_absolute_url(self): 
		return reverse('my_resume_detail', args=[str(self.id)]) 

	class Meta:
		verbose_name = 'Резюме'
		verbose_name_plural = 'Резюме'



class Response(models.Model):
	STATUS_CHOICES = (
			(None,'Не установлен'),
			('student_response','Отклик студента'),
			('offer','Предложение'),
			('reject','Отказ'),
			('offer_completed','Завершенный оффер'),
		)
	resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='responses', verbose_name="Резюме")
	vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE,related_name='responses', verbose_name="Вакансия")
	created_by = models.DateTimeField(auto_now_add=True)
	updated_by =  models.DateTimeField(auto_now=True)
	status = models.CharField('Статус',max_length=30,choices=STATUS_CHOICES, default='published')

	def __str__(self):
		return f'{self.vacancy} <--> {self.resume}'

	class Meta:
		verbose_name = 'Отклик'
		verbose_name_plural = 'Отклики'


class Document(models.Model):
	name = models.CharField('Название',max_length=100,unique=True)
	file = models.FileField('Файл')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Документ'
		verbose_name_plural = 'Документы'





#function to User - Student, Company
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		if instance.role == 'student':
			Student.objects.create(user=instance)
		elif instance.role == 'company':
			Company.objects.create(user=instance)
 
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	if instance.role == 'student':
		instance.students.save()
	elif instance.role == 'company':
		instance.companys.save()

# Create your models here.
