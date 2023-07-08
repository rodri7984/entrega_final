from django import forms
from .models import Marca, Talla, producto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['id_marca','marca']

class TallaForm(forms.ModelForm):
    class Meta:
        model = Talla
        fields = ['id_talla', 'talla']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['id_prod', 'nombre_prod', 'id_marca', 'id_talla', 'color', 'precio', 'imagen']