from django.urls import path
from home.views import index
from home.views import person, ClassPerson

urlpatterns = [
    path('index/', index, name='index'),
    path('person/', person, name='person'),
    path('classperson/', ClassPerson.as_view(),name='classperson')
]
