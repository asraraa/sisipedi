from django.urls import path

from . import views

urlpatterns = [
	#path("<input>", views.withInput, name="withInput"),
	path("create/", views.create, name="create"),
	#path("register/", views.register, name="register"),
	path("register/<int:nip>/", views.register, name='register'),
	path("", views.index, name="index")
]