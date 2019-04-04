from django.core.exceptions import ValidationError
import re
import logging


def validacion_dias_de_la_semana(dia):
    logger = logging.getLogger(__name__)
    logger.setLevel('DEBUG')

    DIAS_DE_LA_SEMANA = {
        ('Lunes'),
        ('Martes'),
        ('Miercoles'),
        ('Jueves'),
        ('Viernes'),
        ('Sabado'),
    }
    # El codigo no esta hecho. Valida las commas pero no valida todas las fechas
    validarMasDeUnaFechaConComma(dia, logger)
    # Eliminar este codigo despues que arregle la funcion
    dias = re.split("[,]", dia)
    if len(dias) > 1:
        return dia

    if not dia.capitalize() in DIAS_DE_LA_SEMANA:
        logger.debug(f"La fecha ingresada no es valida: {dia.capitalize()}")
        raise ValidationError("Una fecha valida debe ser entrada.")
    else:
        return dia



def validarMasDeUnaFechaConComma(dia, logger):
    # Buscar si hay un valor con comma
    dias = re.split("[,]", dia)
    logger.debug(f'Valor del formulario: {dia}')
    if len(dias) > 1:
        return  # Hacer este codigo luego
        logger.debug(f'Dias despues de partilas por las comas: {dias}')
        dia = [dia.capitalize() for dia in dias]
        logger.debug(f"dia despues del list comprehension: {dia}")
        if not (item.capitalize for item in dia) in DIAS_DE_LA_SEMANA:
            logger.debug(f"Una de las fecha no es valida: {tuple(dia)}")
            raise ValidationError("Una de las fechas ingresadas no es valida.")
        else:
            return dia
