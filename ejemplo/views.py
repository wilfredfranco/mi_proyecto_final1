from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

# Create your views here.
def index(request):
    suma = 4 + 3
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":"Wilfred",
        "apellido": suma,
        })

def index_dos(request, nombre, apellido):
    
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre": nombre,
        "apellido": apellido,
        })

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def imc(request, peso, altura):
    altura_metros = altura /100
    peso_kilos = peso / 100
    imc = peso_kilos /altura_metros * altura_metros
    
    return render(request, "ejemplo/imc.html", {"imc": imc})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})
