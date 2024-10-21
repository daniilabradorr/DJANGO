from django.urls import path
from .views import TareaListView, TareaDetailView, TareaCreateView, TareaUpdateView, TareaDeleteView

urlpatterns = [
    path('tareas/', TareaListView.as_view(), name='lista_tareas'),
    path('tareas/<int:pk>/', TareaDetailView.as_view(), name='detalle_tarea'),
    path('tareas/nueva/', TareaCreateView.as_view(), name='crear_tarea'),
    path('tareas/<int:pk>/editar/', TareaUpdateView.as_view(), name='editar_tarea'),
    path('tareas/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='eliminar_tarea'),
]