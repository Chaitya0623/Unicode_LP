from django.forms import ModelForm
from home.models import User, Foreign

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'