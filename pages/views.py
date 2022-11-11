from django.shortcuts import render
from django.views.generic import TemplateView
import random
# Create your views here.

# class HomePageView(TemplateView):
# 	template_name = "pages/home.html"


def home_view(request):
		# template = loader.get_template('pages/home.html')
		print("HELLO")
		numFollowers = random.randint(1000, 5000)
		context= {
			'num_of_followers': numFollowers

		}

		return render(request, 'pages/home.html', context)	


