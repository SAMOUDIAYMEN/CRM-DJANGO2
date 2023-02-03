from django.forms import ModelForm
from django import forms
from Mainapp.models import Project,Customer,Profile,Task,Invoice

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model
User = get_user_model()

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
    
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'customer': forms.Select(attrs={'class':'form-control'}),
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')
    
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'cost_per_houre': forms.TextInput(attrs={'class':'form-control','type' : 'number'}),
            'duration': forms.TextInput(attrs={'class':'form-control','type' : 'number'}),
            'total_cost': forms.TextInput(attrs={'class':'form-control','type' : 'number'}),
        }

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ('__all__')
        
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class':'form-control'}),
            'project': forms.Select(attrs={'class':'form-control'}),
            'invoice_details': forms.Textarea(attrs={'class':'form-control'}),
            'project_duration': forms.TextInput(attrs={'class':'form-control','type' : 'number'}),
            'note': forms.Textarea(attrs={'class':'form-control'}),
        }
        

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name','phone','email')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('is_superuser','user_permissions','first_name','email','mobile','designation','salary','password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'user_permissions' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
        

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user