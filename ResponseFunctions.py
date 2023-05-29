import os, time, string, random, re
from random import randrange
from pokedex import pokedexC


#---------------------------------------#
#  pokedex                              #
#---------------------------------------#
pokedex = pokedexC()


def contar_chiste():
    '''
    Cuenta un chiste de forma aleatoria

    :return El chiste que se va a contar
    :rtype str
    '''
    chistes = [
        'Hay dos personas en un restaurante:\nX-Camarero, traigame una fanta de naranja\nM.-Lo siento señor, no nos queda Fanta, ¿Le va bien un Kas?\nX-Está bien.\nDespués de un rato, el camarero vulve con una fanta. ¿Cómo se llamó el videojuego? \nAl Final Fanta sí.\n', 
        '¿Cuál es el mejor juego de terror de la Wii?\n La Wiija. XD XD XD',
        'Se abre el telón y sale Leonardo Dantés muy constipado. ¿Como se llama el videojuego? Dantés Enfermo.',
        'Esto es una consola de Nintendo sin juegos de Mario. ¿Cómo se llama la película?: "Misión imposible"',
        'Esto es una encuesta de a ver que boss de FF es mas difícil y gana artemisa.'
    ]
    chiste = random.choice(chistes)
    return chiste

def despedida(user_input):
    '''
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    '''
    des = user_input.split()
    despedida_usuario = ['salir', 'adios', 'bye', 'hasta luego', 'adiós']
    despedida_glados = ['Adiós', 'Bye!', '¡Hasta la vista, baby!']
    despedida_definitiva = ''
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva

#-----------------Tipo----------------------#

def dar_tipo_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['tipo'])
    return ''

#-----------------codigo----------------------#

def dar_nombre_numero(nombre):
    '''
    Devuelve el codigo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['num'])
    return ''

#-----------------nombre----------------------#

def dar_numero_nombre(codigo):
    '''
    Devuelve el nombre del pokemon

    :
    '''
    for pokemon in pokedex:
        if pokemon['num'] == codigo:
            return str(pokemon['pokemon'])
    return ''

#-----------------Tipo----------------------#

def dar_tipo_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['tipo'])
    return ''

#-----------------Peso----------------------#

def dar_peso_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['peso'])
    return ''

def dar_peso_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['peso'])
    return ''

#-----------------Altura----------------------#

def dar_altura_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['altura'])
    return ''

def dar_altura_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['altura'])
    return ''

#-----------------Debilidad----------------------#

def dar_debilidad_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['debilidad'])
    return ''

def dar_debilidad_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['debilidad'])
    return ''

#-----------------Fortaleza----------------------#

def dar_fortaleza_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['fortaleza'])
    return ''

def dar_fortaleza_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['fortaleza'])
    return ''

#-----------------Descripcion----------------------#

def dar_descripcion_nombre(nombre):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['pokemon'] == nombre:
            return str(pokemon['descripcion'])
    return ''

def dar_descripcion_numero(numero):
    '''
    Devuelve el tipo del pokemon

    :param str nombre: El nombre del pokemon
    :return El tipo del pokemon
    '''
    for pokemon in pokedex:
        if pokemon['num'] == numero:
            return str(pokemon['descripcion'])
    return ''