
from django.contrib import admin
from django.urls import path ,include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guest', views.Viewsets_guests)
router.register('movies', views.Viewsets_movies)
router.register('reservations', views.Viewsets_reservation, basename="Viewsets_reservation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jasonresponsenomodel/',views.no_rest_no_model),
    path('django/jasonresponsefrommodel', views.no_rest_from_model),
    path('rest/fbv/',views.fbv_list),
    path('rest/fbv/<int:pk>/',views.fbv_pk),
    path('rest/cbv/', views.CBV_List.as_view()),
    path('rest/cbv/<int:pk>/', views.CBV_pk.as_view()),
    path('rest/mixins/', views.Mixins_list.as_view()),
    path('rest/mixins/<int:pk>/', views.Mixins_pk.as_view()),
    path('rest/generics/', views.Generics_list.as_view()),
    path('rest/generics/<int:pk>/', views.Generics_pk.as_view()),
    path('rest/viewsets/',include(router.urls))
]
