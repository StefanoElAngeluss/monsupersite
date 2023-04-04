from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignInForm, SignUpForm, EditProfileForm, PasswordChangedForm, ProfilePageForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Profile

class UserConnexionView(FormView):
  form_class = SignInForm
  template_name = 'registration/connexion.html'
  success_url = reverse_lazy('accueil')

  def form_valid(self, form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(self.request, username=username, password=password)
    if user is not None:
      login(self.request, user)
      return redirect(self.success_url)
    else:
      return self.form_invalid(form)

class UserRegisterView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/inscription.html'
  success_url = reverse_lazy('connexion')

class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('accueil')

  def get_object(self):
    return self.request.user

class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangedForm
  # form_class = PasswordChangeForm
  success_url = reverse_lazy('password_success')

def password_success(request):
  return render(request, 'registration/password_success.html', {})

class CreateProfileDetailView(CreateView):
  model = Profile
  form_class = ProfilePageForm
  template_name = 'profiles/create_profile_utilisateur.html'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class UserProfileDetailView(DetailView):
  model = Profile
  template_name = 'profiles/profile_utilisateur.html'

  def get_context_data(self, *args, **kwargs):
    # users = Profile.objects.all()
    context = super(UserProfileDetailView, self).get_context_data(*args, **kwargs)

    page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

    context['page_user'] = page_user
    return context

class EditProfileDetailView(generic.UpdateView):
  model = Profile
  template_name = 'profiles/edit_profile_utilisateur.html'
  success_url = reverse_lazy('accueil')
  fields = [
    'bio',
    'profile_avatar',
    'facebook_url',
    'github_url',
    'instagram_url',
    'pinterest_url',
    'twitter_url',
    'website_url',
    'youtube_url',
  ]

def get_object(self):
  return self.request.user
