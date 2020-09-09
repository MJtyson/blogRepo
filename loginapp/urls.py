from django.urls import path, include
#from loginapp.views import login_request, logout_request


urlpatterns = [
	#path('',login_request, name = "login"),
	#path('register', register, name = register),
	#path('logout',logout_request, name = "logout"),
    path('', RedirectView.as_view(url='loginapp/', permanent=True)),
    path('loginapp/', include(loginapp.urls)),
]
