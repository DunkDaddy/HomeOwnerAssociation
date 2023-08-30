from django.urls import path
from .views import *

urlpatterns = [
    #se alle data
    path('Bliste/', beboer_liste),
    path('Lliste/', location_liste),
    path('Rliste/', regler_liste),
    path('Aliste/', andmeldelse_liste),

    path('Bcreate/', beboer_create),
    path('Lcreate/', location_create),
    path('Rcreate/', regler_create),
    path('Acreate/', andmeldelse_create),

    path('B/<int:pk>/', beboer_view),
    path('L/<int:pk>/', location_view),
    path('R/<int:pk>/', regler_view),
    path('A/<int:pk>/', andmeldelse_view),

    path('Bupdate/<int:pk>/', beboer_update),
    path('Lupdate/<int:pk>/', location_update),
    path('Rupdate/<int:pk>/', regler_update),
    path('Aupdate/<int:pk>/', andmeldelse_update),


    path('Bdelete/<int:pk>/', beboer_delete),
    path('Ldelete/<int:pk>/', location_delete),
    path('Rdelete/<int:pk>/', regler_delete),
    path('Adelete/<int:pk>/', andmeldelse_delete),

    path('password/', password_check)
]