from django.conf import settings
from django.urls import path
from students.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", home, name="index"),
    path("add_student/", add_student, name="studentslist"),
    path("delete_student/<rollno>", delete_student, name="delete_student"),
    path("update_student/<rollno>", update_student, name="update_student"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
