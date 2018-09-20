from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('patron/', views.RegisterPatron.as_view(), name='register_patron_view'),
	# path('associates/', views.RegisterAssociates.as_view(), name='register_associates_view'),
	path('pdf/',views.GeneratePdf.as_view()),
]