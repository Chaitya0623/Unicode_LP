from django.forms import ModelForm
from home.models import User, MyUser

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# class MyUserForm(ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ('email')