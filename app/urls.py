from django.urls import path
from .views import deletetodo, home,finishtodo,updatetodo
urlpatterns = [
    path('',home),
    path('delete/<int:id>/',deletetodo),
    path('finish/<int:id>/',finishtodo),
    path('update/<int:id>/',updatetodo)
]
