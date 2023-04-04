from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

class SignInForm(forms.Form):
  username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'password')

  def __init__(self, *args, **kwargs):
    super(SignInForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password'].widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'

class PasswordChangedForm(PasswordChangeForm):
  old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

  class Meta:
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')

class EditProfileForm(UserChangeForm):
  username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  # dernière_connexion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  # is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  # is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  # is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
  # date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name')
    # fields = ('username', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active')

class ProfilePageForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('bio', 'profile_avatar', 'facebook_url', 'github_url', 'instagram_url', 'pinterest_url', 'twitter_url', 'website_url', 'youtube_url')

    widgets = {
      'bio': forms.Textarea(attrs={'class': 'form-control'}),
      'profile_avatar': forms.FileInput(attrs={'class': 'form-control'}),
      'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
      'github_url': forms.TextInput(attrs={'class': 'form-control'}),
      'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
      'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
      'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
      'website_url': forms.TextInput(attrs={'class': 'form-control'}),
      'youtube_url': forms.TextInput(attrs={'class': 'form-control'}),
    }

class EditProfileDetailForm(UserChangeForm):
  bio = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control'}))
  facebook_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  github_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  instagram_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  pinterest_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  twitter_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  website_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  youtube_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('bio', 'facebook_url', 'github_url', 'instagram_url', 'pinterest_url', 'twitter_url', 'website_url', 'youtube_url')