from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from tasks.models import Task
    

class SignupForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    """
        
class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SigninForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'
    """

class TaskForm (forms.ModelForm):
    
    class Meta:
        model=Task
        fields =['title','description', 'important']
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'select a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

