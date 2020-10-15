from django.urls import path


from .views import TodoListAPIView, TodoDetailAPIView, TodoDestroyAPIView


app_name = 'todos'


urlpatterns = [
    path('<int:pk>/', TodoDetailAPIView.as_view(), name="todo_detail"),
    path ('<int:pk>/', TodoDestroyAPIView.as_view(), name="todo_destroy"),
    path('', TodoListAPIView.as_view(), name="todo_list"),
]
