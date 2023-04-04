from .views import CreateProfileDetailView, UserConnexionView, UserRegisterView, UserEditView, PasswordsChangeView, UserProfileDetailView, EditProfileDetailView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
  path('connexion/', UserConnexionView.as_view(), name='connexion'),
  path('inscription/', UserRegisterView.as_view(), name='inscription'),
  path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
  path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
  path('password_success', views.password_success, name='password_success'),
  path('<int:pk>/profile/', UserProfileDetailView.as_view(), name='profile_utilisateur'),
  path('<int:pk>/edit_profile_utilisateur/', EditProfileDetailView.as_view(), name='edit_profile_utilisateur'),
  path('<int:pk>/edit_profile_utilisateur/', EditProfileDetailView.as_view(), name='edit_profile_utilisateur'),
  path('<int:pk>/create_profile_utilisateur/', CreateProfileDetailView.as_view(), name='create_profile_utilisateur'),
] + static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT
  )