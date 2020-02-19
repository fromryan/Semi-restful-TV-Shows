from django.urls import path
from . import views

urlpatterns = [
	path('show/new', views.index),
    path('create', views.create),
    path('show/<int:id>', views.info),
    path('show/<int:id>/edit', views.edit),
    path('show/<int:id>/update', views.update),
    path('show/<int:id>/delete', views.delete),
    path('shows', views.shows),
    # path('')
]