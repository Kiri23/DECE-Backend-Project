from django import forms
from .models import Registracion

GENEROS = [
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Otros', 'Otro'),
]

PREPARACION_ACADEMICA = [
    ('', 'Seleciona una opción'),
    ('Noveno', 'Noveno grado'),
    ('Decimo', 'Decimo grado'),
    ('Certificado', 'Certificado'),
    ('Grado asociado', 'Grado asociado'),
]

# Semantic UI

# Hacer un Init method que marque a todos como required


class InscribeteForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'nombre', 'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'apellido', 'class': 'form-control'}))
    correo_electronico = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'ejemplo@gmail.com', 'class': 'form-control text-input w-75'}))
    generos = forms.CharField(widget=forms.RadioSelect(
        attrs={'class': 'form-check-input'}, choices=GENEROS), required=True)
    fecha_de_nacimiento = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'name': 'fecha-de-nacimiento', 'class': 'form-control', 'type': 'date'}), required=True)
    lugar_de_nacimiento = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ingresa una ubicación', 'class': 'form-control', 'name': 'lugar-de-nacimiento', 'id': 'autocomplete'}), required=True)
    numero_de_telefono = forms.RegexField(regex='\d{5}', widget=forms.TextInput(
        attrs={'name': 'telefono', 'type': 'tel', 'placeholder': 'Ejemplo (787)-555-9876', 'class': 'form-control w-75', 'id': 'telefono', 'size': '300', 'pattern': '\d{5}'}), required=True, label='Telefono:', help_text='Por si necesitamos comunicarnos con usted')
    preparacion_academica = forms.ChoiceField(choices=PREPARACION_ACADEMICA, widget=forms.Select(
        attrs={'class': 'custom-select'}), required=True)
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'direcion', 'class': 'form-control'}), required=True, help_text='Ejemplo: Urb.Estancias Calle San Antonio 123')
    pueblo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-input'}), required=True)
    pais = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    zip_code = forms.CharField(widget=forms.TextInput(
        attrs={'name':'zipcode','id':'zipcode','type':'tel','placeholder': 'XXXXX', 'class': 'form-control', 'pattern': '\d{5}'}), required=True)
    ocupacion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    telefono_del_trabajo = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'telefono-del-trabajo', 'id': 'telefono-del-trabajo', 'type': 'tel', 'placeholder': '(XXX)XXX-XXXX', 'class': 'form-control', 'pattern': '\d{5}'}),required=True)
    lugar_del_trabajo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}),required=True)
    class Meta:
        model = Registracion
        # Excluye el curso y el estudiante del form y de la validacion. OJO! si remueve uno de los dos el form no se va a crear porque esta esperando que algunos de esos dos valores se llenen mediante el formulario en html. 
        exclude = ['curso','estudiante']
        # fields = ['nombre', 'apellido', 'correo_electronico','fecha_de_nacimiento','lugar_de_nacimiento','numero_de_telefono','preparacion_academica','direccion','pueblo','pais','zip_code','ocupacion','telefono_del_trabajo','lugar_del_trabajo']
