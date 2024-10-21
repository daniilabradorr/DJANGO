from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Tarea

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

@method_decorator(login_required, name='dispatch')  # Decorador para requerir autenticación
class TareaListView(ListView):
    model=Tarea
    template_name="tareas/tarea_list.html"
    context_object_name = 'tareas'
    
    
    def get_queryset(self):
        queryset = Tarea.objects.filter(usuario=self.request.user)
        prioridad = self.request.GET.get('prioridad')
        completada = self.request.GET.get('completada')

        if prioridad:
            queryset = queryset.filter(prioridad=prioridad)
        if completada:
            queryset = queryset.filter(completada=(completada == 'true'))

        return queryset  # Mostrar solo tareas del usuario logueado

@method_decorator(login_required, name='dispatch')
class TareaDetailView(DetailView):
    model=Tarea
    template_name="tareas/tarea_detail.html"
    context_object_name='tarea'

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)#Aseguramos que el usuario solo veas sus tareas.

@method_decorator(login_required, name='dispatch')    
class TareaCreateView(CreateView):
    model=Tarea
    template_name="tareas/tarea_create.html"
    fields= ['titulo','descripcion','prioridad']
    success_url=reverse_lazy('lista_tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user #Asigna al usuario al crear la tarea
        messages.success(self.request, 'La tarea ha sido creada con éxito.')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TareaUpdateView(UpdateView):
    model = Tarea
    template_name="tareas/tarea_update.html"
    fields= ['titulo','descripcion','prioridad','completada']
    success_url=reverse_lazy('lista_tareas')

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user) #Asegura que el usuario solo actualice sus propias tareas
    
    def form_valid(self, form):
        tarea = form.save(commit=False)
        if tarea.completada:
            # Eliminar la tarea después de 2 días
            tarea.fecha_completada = timezone.now() + timedelta(days=2)
        tarea.save()
        messages.success(self.request, 'La tarea ha sido actualizada con éxito.')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tareas/tarea_delete.html"
    success_url = reverse_lazy('lista_tareas')

    def get_queryset(self): #Asegura que se elimine la tarea de ese usuario.
        return Tarea.objects.filter(usuario=self.request.user)
    
