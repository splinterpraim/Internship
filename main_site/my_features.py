from django.shortcuts import render, redirect
from .models import CustomUser, Student, Company

class ProfileHelp():
	def __init__(self,request, user_render=False):
		self.request = request
		self.user = CustomUser.objects.get(id=request.user.id)
		if self.user.role == 'student':
			self.profile = Student.objects.get(id=self.user.students.id)
			self.profile_template = 'main_site/profile/profile_student.html'
		if self.user.role == 'company':
			self.profile = Company.objects.get(id=self.user.companys.id)
			self.profile_template = 'main_site/profile/profile_company.html'
		self.form = ''
		self.error = ''
		self.context = dict()
		self.user_render = user_render
		self.view_role = 'student'


	def main(self):
		if self.check_view_role():
			if self.request.method == 'POST':
				self.method_POST()
				if self.error == '':
					return redirect('profile')
			else:
				self.method_GET()
			return render(self.request,self.profile_template,self.get_context())
		else:
		 	return redirect('profile')


	def check_view_role(self):
		if self.view_role == self.user.role:
			return True
		elif self.view_role == 'both':
			return True
		else:
			return False


	def get_context(self):
		self.context['section'] = "profile"
		self.context['form'] = self.form
		self.context['user']= self.user 
		self.context['error']= self.error
		if self.user.role == 'student':
			self.context['student'] = self.profile
		if self.user.role == 'company':
			self.context['company'] = self.profile
		return self.context

	def add_context(self,context):
		self.context = context.copy()

	def method_POST(self):
		self.form = self.form(self.request.POST, self.request.FILES)
		if self.form.is_valid():
			self.choise_func(self.form.get_func_name())
		else:
			self.error = 'не правильные данные'
			
		
	def method_GET(self):
		if self.user_render:
			self.form = self.form(instance=self.user)
		else:
			self.form = self.form(instance=self.profile)
		self.form.save(commit=False)
		


	def choise_func(self,func_name):
		if func_name == 'save_full_name':
			self.save_full_name()
		elif func_name == 'save_date_of_birth':
			self.save_date_of_birth()
		elif func_name == 'save_phone':
			self.save_phone()
		elif func_name == 'save_group':
			self.save_group()
		elif func_name == 'save_username':
			self.save_username()
		elif func_name == 'save_name':
			self.save_name()
		elif func_name == 'save_photo':
			self.save_photo()
		elif func_name == 'save_description':
			self.save_description()
		elif func_name == 'save_address':
			self.save_address()
		elif func_name == 'save_site_name':
			self.save_site_name()



	def save_full_name(self):
		cd = self.form.cleaned_data
		self.user.students.name= cd['name']
		self.user.students.last_name= cd['last_name']
		self.user.students.father_name= cd['father_name']
		self.user.save()

	def save_date_of_birth(self):
		cd = self.form.cleaned_data
		self.user.students.date_of_birth= cd['date_of_birth']
		self.user.save()

	def save_phone(self):
		cd = self.form.cleaned_data
		if self.user.role == 'student':	
			self.user.students.phone = cd['phone']
		elif self.user.role == 'company':
			self.user.companys.phone = cd['phone']	
		self.user.save()

	def save_group(self):
		cd = self.form.cleaned_data
		self.user.students.university_group= cd['university_group']
		self.user.save()

	def save_username(self):
		cd = self.form.cleaned_data
		self.user.username= cd['username']
		self.user.save()

	def save_name(self):
		self.form.save()
		# cd = self.form.cleaned_data
		# self.user.companys.name= cd['name']
		# self.user.save()

	def save_photo(self):
		cd = self.form.cleaned_data
		self.user.companys.photo= cd['photo']
		self.user.save()

	def save_description(self):
		cd = self.form.cleaned_data
		self.user.companys.description = cd['description']
		self.user.save()


	def save_address(self):
		cd = self.form.cleaned_data
		self.user.companys.address = cd['address']
		self.user.save()

	def save_site_name(self):
		cd = self.form.cleaned_data
		self.user.companys.site_name = cd['site_name']
		self.user.save()	
