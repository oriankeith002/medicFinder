from django.urls import path 
from msearch.views.ProfileView import list_profile_view


app_name = 'msearch' 


url_patterns = [
    
    path("",list_profile_view),
    path("<int:id>", list_profile_view),
]