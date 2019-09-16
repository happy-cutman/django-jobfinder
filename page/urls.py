from django.urls import path

from .views import *


urlpatterns = [
	path('', index_page, name='index_page_url'),
	path('result/kiev_python/', kiev_python, name='kiev_python_url'),
	path('result/kiev_javascript/', kiev_javascript, name='kiev_javascript_url'),
	path('result/kiev_java/', kiev_java, name='kiev_java_url'),
	path('result/kiev_c_sharp/', kiev_c_sharp, name='kiev_c_sharp_url'),
]
