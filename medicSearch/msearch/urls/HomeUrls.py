from django.urls import path 
from msearch.views.HomeView import home_view


app_name = 'msearch' 


url_patterns = [
    
    path("",home_view),
]