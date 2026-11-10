from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import MovimientoForm
from .models import Movimiento

import requests


@login_required(login_url='/cuentas/login/')
def inicio(request):
    movimientos = Movimiento.objects.filter(
        usuario=request.user
    ).order_by('-fecha', '-id')

    ingresos = sum(
        movimiento.monto
        for movimiento in movimientos
        if movimiento.tipo == 'ingreso'
    )

    gastos = sum(
        movimiento.monto
        for movimiento in movimientos
        if movimiento.tipo == 'gasto'
    )

    saldo = ingresos - gastos

    # Consulta del tipo de cambio mediante Frankfurter API
    tipo_cambio = None
    fecha_cambio = None

    try:
        respuesta = requests.get(
            'https://api.frankfurter.dev/v1/latest?base=USD&symbols=MXN',
            timeout=10
        )
        respuesta.raise_for_status()

        datos = respuesta.json()
        tipo_cambio = datos['rates']['MXN']
        fecha_cambio = datos['date']

    except (requests.RequestException, KeyError, ValueError):
        tipo_cambio = None
        fecha_cambio = None

    return render(
        request,
        'finanzas/inicio.html',
        {
            'movimientos': movimientos,
            'ingresos': ingresos,
            'gastos': gastos,
            'saldo': saldo,
            'tipo_cambio': tipo_cambio,
            'fecha_cambio': fecha_cambio,
        }
    )


@login_required(login_url='/cuentas/login/')
def agregar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)

        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user
            movimiento.save()

            return redirect('inicio')
    else:
        form = MovimientoForm()

    return render(
        request,
        'finanzas/agregar_movimiento.html',
        {'form': form}
    )


@login_required(login_url='/cuentas/login/')
@require_POST
def eliminar_movimiento(request, id):
    movimiento = get_object_or_404(
        Movimiento,
        id=id,
        usuario=request.user
    )

    movimiento.delete()

    return redirect('inicio')
