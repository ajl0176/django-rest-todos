from django.urls import path, include

app_name = 'api_v1'

urlpatterns = [
    path('todos/', include('todos.urls', namespace='todos')),
]
