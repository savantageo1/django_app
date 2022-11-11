from django.urls import path
# from .views import HomePageView
from pages import views


urlpatterns = [
	path('home', views.home_view),
	# path("", HomePageView.as_view(), name="home"),
]