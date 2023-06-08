from django.urls import path
from api.views  import UserLCView, UserRUDView, PetLCView, PetRUDView

urlpatterns = [
    path('postapi/', UserLCView.as_view() , name = "user-list-create"),
    path('postapi/<int:pk>', UserRUDView.as_view() , name = "user-list-update-destroy"),
    
 #############################################################################################
    
    
    path('petapi/', PetLCView.as_view() , name = "user-list-create"),
    path('petapi/<int:pk>', PetRUDView.as_view() , name = "user-list-update-destroy")
    
     
     
    
]
