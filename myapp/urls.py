from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('contact/',views.contact,name="contact"),
     path('signup/',views.signup,name="signup"),
]