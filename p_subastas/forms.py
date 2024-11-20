from django import forms

class OfertaForm1(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label="Nombre completo")
    dui_nit = forms.CharField(max_length=25, label="DUI o NIT (Sin guiones)")
    correo = forms.EmailField(label="Correo electrónico")
    teléfono = forms.CharField(max_length=25, label="Teléfono")
    oferta = forms.CharField(max_length=12, label="Valor a Ofertar")

class OfertaForm2(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label="Nombre completo")
    dui_nit = forms.CharField(max_length=25, label="DUI o NIT (Sin guiones)")
    correo = forms.EmailField(label="Correo electrónico")
    teléfono = forms.CharField(max_length=25, label="Teléfono")
    oferta = forms.CharField(max_length=12, label="Valor a Ofertar")
class OfertaFormx(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label="Nombre completo")
    dui_nit = forms.CharField(max_length=25, label="DUI o NIT (Sin guiones)")
    correo = forms.EmailField(label="Correo electrónico")
    teléfono = forms.CharField(max_length=25, label="Teléfono")
    oferta = forms.CharField(max_length=12, label="Valor a Ofertar")