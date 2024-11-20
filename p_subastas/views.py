from django.shortcuts import render
from .forms import OfertaForm1, OfertaForm2, OfertaFormx
from .models import Oferta
from django.db import IntegrityError

def ofertar(request):
    form1 = OfertaForm1()
    form2 = OfertaForm2()
    formx = OfertaFormx()
    message = None
    success = False
    form_submitted = False

    # Si el método es POST, procesar la información
    if request.method == 'POST':
        # Procesamos el formulario que se haya enviado
        if 'form1_submit' in request.POST:
            form = OfertaForm1(request.POST)
            artículo = "2015 TOYOTA CAMRY LE"
            id_vehicular = "4T1BF1FK5FU******"
            kilometraje = "165,601 mi(ACTUAL)"
            form_submitted = True
        elif 'form2_submit' in request.POST:
            form = OfertaForm2(request.POST)
            artículo = "2016 MITSUBISHI OUTLANDER SE"
            id_vehicular = "JA4AD3A30GZ******"
            kilometraje = "119,999 mi(ACTUAL)"
            form_submitted = True
        elif 'formx_submit' in request.POST:
            form = OfertaFormx(request.POST)
            artículo = "DJI Mini 2 SE"
            id_vehicular = "No aplica"
            kilometraje = "No aplica"
            form_submitted = True
        else:
            form = None

        # Si el formulario es válido, procesamos los datos
        if form:
            if form.is_valid():
                dui_nit = form.cleaned_data['dui_nit']
                correo = form.cleaned_data['correo']


                if not correo or not dui_nit:
                    message = 'Todos los campos son obligatorios.'
                else:
                    if Oferta.objects.filter(artículo=artículo, correo=correo).exists() or \
                       Oferta.objects.filter(artículo=artículo, dui_nit=dui_nit).exists():
                        message = 'Ya se registró una oferta con estos datos.'
                    else:
                        try:
                            # Crear la oferta en la base de datos
                            Oferta.objects.create(
                                nombre_completo=form.cleaned_data['nombre_completo'],
                                dui_nit=dui_nit,
                                correo=correo,
                                teléfono=form.cleaned_data['teléfono'],
                                oferta=form.cleaned_data['oferta'],
                                artículo=artículo,
                                id_vehicular=id_vehicular,
                                kilometraje=kilometraje
                            )
                            # Después de una oferta exitosa, redirige para evitar reenvíos
                            return render(request, 'Subasta_exitosa.html')  # Redirige a la página de éxito
                        except IntegrityError:
                            message = 'Error al guardar la oferta, intente nuevamente.'
            else:
                message = 'El formulario no es válido. Verifique los datos ingresados.'

    # Si no es un POST o el formulario no se ha procesado correctamente, renderiza el formulario.
    return render(request, 'P_Subastas.html', {
        'form1': form1,
        'form2': form2,
        'formx': formx,
        'message': message,
        'success': success,
        'form_submitted': form_submitted,
    })


    