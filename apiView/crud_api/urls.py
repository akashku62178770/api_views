from django.urls import path 
from .views import StudentView, StudentMixinView, StudentRetrieveMixinView, StudentGenericView, StudentDataGenericsView

urlpatterns = [
    # API View Paths
    path("getStudents/", StudentView.as_view(), name="getStudents"), 
    path("getStudents/<int:id>/", StudentView.as_view(), name="getStudents"), 
    # Mixin paths 
    path("studentsList/", StudentMixinView.as_view(), name="studentsList"), 
    path("studentRetrieve/<int:id>", StudentRetrieveMixinView.as_view(), name="studentRetrieve"),
    # Generic paths
    path("studentData/", StudentGenericView.as_view(), name="studentData"),
    path("fetchStudent/<int:pk>", StudentDataGenericsView.as_view(), name="fetchStudent"),
]
# getStudents/3