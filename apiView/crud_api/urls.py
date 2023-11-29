from django.urls import path 
from .views import StudentView, StudentMixinView, StudentRetrieveMixinView

urlpatterns = [
    path("getStudents/", StudentView.as_view(), name="getStudents"), 
    path("getStudents/<int:id>/", StudentView.as_view(), name="getStudents"), 
    # Mixin paths 
    path("studentsList/", StudentMixinView.as_view(), name="studentsList"), 
    path("studentRetrieve/<int:id>", StudentRetrieveMixinView.as_view(), name="studentRetrieve"),

]
# getStudents/3