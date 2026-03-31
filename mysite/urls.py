from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import home, success, contact, about, test
from vege.views import login_page, receipes, delete_receipe, update_receipe, register, logout_page, get_students, see_marks
from home.views import send_email

urlpatterns = [
    path('', home , name="home"),
    path('test/', test, name="test"),
    path('login/', login_page ,name="login_page"),
    path('register/',register,name="register_page"),
    path('receipes/', receipes, name="receipes"),
     
    path('delete-receipe/<int:id>/',delete_receipe, name="delete_receipe"),
    path('update-receipe/<int:id>/',update_receipe, name="update_receipe"),
    
    path('success-page/', success , name="success"),

    path('students/', get_students, name="successs_page"),
    path('see_marks/<str:student_id>/', see_marks, name="see_marks"),
   
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('logout/',logout_page, name="logout_page"),
    path('send-email/', send_email, name='send_email')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()