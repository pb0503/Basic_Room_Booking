"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import room.views as views
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('home', views.homepage,name="homepage"),
    path('user/bookings', views.user_bookings,name="dashboard"),
    path('user/book-room', views.book_room_page,name="bookroompage"),
    path('user/book-room/book', views.book_room,name="bookroom"),
    path('staff/panel', views.panel,name="staffpanel"),
    path('staff/allbookings', views.all_bookings,name="allbookigs"),
    path('staff/panel/add-new-location', views.add_new_location,name="addnewlocation"),
    path('staff/panel/edit-room', views.edit_room),
    path('staff/panel/add-new-room', views.add_new_room,name="addroom"),
    path('staff/panel/edit-room/edit', views.edit_room),
    path('staff/panel/view-room', views.view_room),
    path('admin/', admin.site.urls),
    

]
