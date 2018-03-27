from django.shortcuts import render, get_object_or_404
from .models import Trabajador
from .forms import FormTrabajador
from django.shortcuts import redirect

def listar_trabajadores(request):
    form = FormTrabajador()
    trabajadores = Trabajador.objects.all()
    return render(request, 'crudTrabajadores/trabajadores.html', {'trabajadores': trabajadores, 'form':form})

def nuevo_trabajador(request):
    if request.method == "POST":
        form = FormTrabajador(request.POST)
        if form.is_valid():
            trabajador = form.save(commit=False)
            trabajador.author = request.user
            trabajador.save()
            return redirect('listado')
    else:
        form = FormTrabajador()
    return render(request, 'crudTrabajadores/nuevo_trabajador.html', {'form': form})

def actualizar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == "POST":
        form = FormTrabajador(request.POST, instance=trabajador)
        if form.is_valid():
            trabajador = form.save(commit=False)
            trabajador.author = request.user
            trabajador.save()
            return redirect('listado')
    else:
        form = FormTrabajador(instance=trabajador)
    return render(request, 'crudTrabajadores/nuevo_trabajador.html', {'form': form})

def borrar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    trabajadorBorrar = Trabajador.objects.get(pk=pk)
    trabajadorBorrar.delete()
    trabajadores = Trabajador.objects.all()
    return render(request, 'crudTrabajadores/trabajadores.html', {'trabajadores':trabajadores})
