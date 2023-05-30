#------------------------------------------------#
#  ChatBot.py                                     #
#------------------------------------------------#

import numpy as np
import re, random, sys
from conocimiento import conocimientoT
from ResponseFunctions import contar_chiste, despedida, dar_tipo_nombre, dar_tipo_numero,dar_nombre_numero,dar_numero_nombre, dar_peso_nombre, dar_peso_numero, dar_altura_nombre, dar_altura_numero, dar_debilidad_nombre, dar_debilidad_numero, dar_fortaleza_nombre, dar_fortaleza_numero, dar_descripcion_nombre, dar_descripcion_numero
from pokedex import pokemonesC


class ChatBot:
    """
    Clase ChatBot para simular una conversación 
    sobre pokemones con un usuario, dando información como si fuera una pokedex.

    :param str contexto: El contexto actual de la conversación
    :param str entrada: El texto escrito por el usuario
    """
    contexto = "DEFAULT"
    entrada = ""

    def __init__(self):
        """
        ChatBot consta de una base de conocimiento
        representada como una lista de casos o intents.
        """ 
        '''
        ##-------------------------------------- codigo para encontrar intent usando expresiones regulares
        self.conocimiento = [] 
        for caso in conocimiento:
            caso['regex'] = list(map(lambda x:re.compile(x, re.IGNORECASE), caso['regex']))
            self.conocimiento.append(caso)
        '''
        ##-------------------------------------- codigo para encontrar intent usando vector
        self.conocimiento = []
        for caso in conocimiento:
            self.conocimiento.append(caso)

    def responder(self, user_input):
        '''
        Flujo básico para identificar coincidencias de intents para responder al usuario.
        Con el texto del usuario como parámetro, los paso a realizarse son:
        1. Encontrar el caso de la base de conocimiento usando expresiones regulares
        2. Si es necesario, realizar acciones asociadas al intent (por ejemplo: consultar información adicional)
        3. Seleccionar una respuesta de la lista de respuestas según el caso del intent
        4. Si es necesario, identificar los parámetros o entidades del texto para dar formato a la respuesta seleccionada
        5. Devolver la respuesta

        :param str user_input: El texto escrito por el usuario
        :return Un texto de respuesta al usuario
        :rtype: str
        '''
        caso = self.encontrar_intent(user_input)
        self.identifica_contexto(caso) 
        informacion_adicional = self.acciones(caso, user_input)
        respuesta = self.convertir_respuesta(random.choice(caso['respuesta']), caso, user_input)
        respuesta_final = (respuesta + '\n' + informacion_adicional).strip() 
        return respuesta_final
    
    def split_user_inputV(self, user_input):
        archivo = open('intentsPokeC.csv', 'r')  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
        try:
            primera_linea = archivo.readline().strip()
            opciones = primera_linea.split(',')
            print( str(opciones) )
        finally:
            archivo.close()
        transformada = [0]*len(opciones)
        ## -------------------------------------- codigo para crear vector  a partir del user input
        for i, palabra in enumerate(opciones):
            if palabra in user_input:
                transformada[i] = 1
        return transformada

    def encontrar_intentV(self, user_input):
        archivo = open('intentsPokeC.csv', 'r')  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
        lineas = []
        minDist = 100000000
        intent = ""
        transformada = self.split_user_inputV(user_input)
        try:
            next(archivo)
            for linea in archivo:
                linea_array = linea.split(',')
                inte = linea_array.pop(0)
                ##AGREGA AQUÍ EL CÓDIGO PARA LEER LAS LÍNEAS, NOTA QUE ESTO ES SOLO UNA BASE, POR LO QUE PARA LLEGAR AL CÁLCULO DEL VECTOR DEBERÁS PROCESAR DE FORMA CORRECTA LA LÍNEA DEL ARCHIVO ANTES DE HACER EL CÁLCULO.
                a = np.array(linea_array)
                b = np.array(transformada)
                a = a.astype(int)
                b = b.astype(int)
                dist = np.linalg.norm(a-b) ## distancia entre vectores
                if dist < minDist:
                    minDist = dist
                    intent = inte
        finally:
            archivo.close()
        return intent

    def encontrar_intent(self, user_input):
        '''
        Encuentra el caso o intent asociado en la base de conocimiento

        :param str user_input: El texto escrito por el usuario
        :return El diccionario que representa el caso o intent deseado
        :rtype: str
        '''
        '''
        ##-------------------------------------- codigo para encontrar intent usando expresiones regulares

        for caso in self.conocimiento:
            for regularexp in caso['regex']:
                match = regularexp.match(user_input)
                if match:
                    self.regexp_selected = regularexp 
                    return caso
        '''
        ##-------------------------------------- codigo para encontrar intent usando distancia entre vectores
        intent_usuario = self.encontrar_intentV(user_input)
        for caso in self.conocimiento:
            if caso['intent'] == intent_usuario:
                return caso
        return {}

    def identifica_contexto(self, caso):
        '''
        Asegura que el contexto sea el adecuado para que
        ChatBot responde de manera coherente

        :param dict caso: El intent del cual se solicita información 
        '''
        intent = caso['intent']
        if intent == 'bienvenida':
            self.contexto = "BIENVENIDA"
        elif intent == 'tipo':
            self.contexto = "TIPO"
        elif intent == 'peso':
            self.contexto = "PESO"
        elif intent == 'altura':
            self.contexto = "ALTURA"
        elif intent == 'debilidad':
            self.contexto = "DEBILIDAD"
        elif intent == 'fortaleza':
            self.contexto = "FORTALEZA"
        elif intent == 'descripcion':
            self.contexto = "DESCRIPCION"
        elif intent == 'codigo':
            self.contexto = "CODIGO"
        elif intent == 'nombre':
            self.contexto = "NOMBRE"
        elif intent == 'desconocido':
            self.contexto = "DEFAULT"  

    def convertir_respuesta(self, respuesta, caso, user_input):
        '''
        Cambia los textos del tipo %1, %2, %3, etc., por su correspondiente propiedad
        identificada en los grupos parentizados de la expresión regular asociada.

        :param str respuesta: Una respuesta que desea convertirse
        :param dict caso: El caso o intent asociado a la respuesta
        :param str user_input: El texto escrito por el usuario
        :return La respuesta con el cambio de parámetros
        :rtype: str
        '''
        respuesta_cambiada = respuesta
        intent = caso['intent']
        '''
        ##-------------------------------------- codigo para encontrar intent usando expresiones regulares
        match = self.regexp_selected.match(user_input)
        '''
        ##-------------------------------------- codigo para encontrar intent usando distancia entre vectores
        for regularExp in caso['regex']:
            regex = re.compile(regularExp, re.IGNORECASE)
            match = regex.match(user_input)
            if match:
                if intent == 'tipo':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                elif intent == 'peso':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                elif intent == 'altura':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                elif intent == 'debilidad':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                elif intent == 'fortaleza':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                elif intent == 'descripcion':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre o numero del Pokémon"
                if intent == 'codigo':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el nombre del Pokémon"
                if intent == 'nombre':
                    if self.obtener_nombre_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_nombre_pokemon(user_input))
                    elif self.obtener_numero_pokemon(user_input) != None:
                        respuesta_cambiada = respuesta_cambiada.replace('%1', self.obtener_numero_pokemon(user_input))
                    else:
                        respuesta_cambiada = "No se encontró el código del Pokémon"                
        return respuesta_cambiada
    

    def obtener_nombre_pokemon(self, user_input):
    # Expresión regular para buscar los nombres de Pokémon
        patron = r"\b(" + "|".join(pokemones) + r")\b"
        p = re.compile(patron, re.IGNORECASE)
        u_i = re.compile(user_input, re.IGNORECASE)
    # Buscar el nombre de Pokémon en la cadena
        resultado = re.search(patron, user_input, re.IGNORECASE)
        if resultado:
            return resultado.group(0)
        else:
            return None
        
    def obtener_numero_pokemon(self, user_input):
    # Expresión regular para buscar los nombres de Pokémon
        patron = r'[0-9][0-9][0-9]'
        p = re.compile(patron, re.IGNORECASE)
        u_i = re.compile(user_input, re.IGNORECASE)
    # Buscar el nombre de Pokémon en la cadena
        resultado = re.search(patron, user_input, re.IGNORECASE)
        if resultado:
            return resultado.group(0)
        else:
            return None

    def acciones(self, caso, user_input):
        '''
        Obtiene información adicional necesaria para dar una respuesta coherente al usuario.
        El tipo de acciones puede ser una consulta de información, revisar base de datos, generar
        un código, etc. y el resultado final es expresado como una cadena de texto

        :param dict caso: El caso o intent asociado a la respuesta
        :return Texto que representa información adicional para complementar la respuesta al usuario
        :rtype: str
        '''
        intent = caso['intent']
        if intent == 'tipo':
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_tipo_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_tipo_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''        
        elif intent == 'peso': 
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_peso_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_peso_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        elif intent == 'altura': 
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_altura_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_altura_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        elif intent == 'debilidad': 
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_debilidad_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_debilidad_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        elif intent == 'fortaleza': 
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_fortaleza_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_fortaleza_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        elif intent == 'descripcion': 
            if self.obtener_nombre_pokemon(user_input) != None:
                #return 'entre en tipo nombre'
                return dar_descripcion_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                #return 'entre en tipo numero'
                return dar_descripcion_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        if intent == 'codigo':
            if self.obtener_nombre_pokemon(user_input) != None:
                return dar_nombre_numero(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                return dar_nombre_numero(self.obtener_numero_pokemon(user_input))
            if self.obtener_nombre_pokemon(user_input) != None:
                return dar_nombre_numero(self.obtener_numero_pokemon(user_input))
            else:
                return ''
        if intent == 'nombre':
            if self.obtener_nombre_pokemon(user_input) != None:
                return dar_numero_nombre(self.obtener_nombre_pokemon(user_input))
            elif self.obtener_numero_pokemon(user_input) != None:
                return dar_numero_nombre(self.obtener_numero_pokemon(user_input))
            if self.obtener_nombre_pokemon(user_input) != None:
                return dar_numero_nombre(self.obtener_numero_pokemon(user_input))
            else:
                return ''                           
        elif intent == 'terminar':
            #print(despedida(user_input))
            #sys.exit(0)

            #se despide pero no se cierre el programa
            return despedida(user_input)
        return ''


    def da_respuesta_apropiada(self, user_input):
        '''
        Devuelve la respuesta según el contexto en el que se encuentre

        :param str user_input: El texto escrito por el usuario
        :return Texto que representa la respuesta
        :rtype str
        '''
        if self.contexto == 'CHISTE':
            return 'Aquí va otro: ' + contar_chiste()
        elif self.contexto == 'DEFAULT':
            return '¿Podrías tratar de expresarte mejor?'
        else:
            return '¿Podrías tratar de expresarte mejor?'

#---------------------------------------#
#  Base de conocimiento                 #
#---------------------------------------#
conocimiento = conocimientoT()


#---------------------------------------#
#  pokemones                            #
#---------------------------------------#
pokemones = pokemonesC()



#---------------------------------------#
#  Interfaz de texto                    #
#---------------------------------------#
def chatBot():
    input_usuario = ''
    asistente = ChatBot()    
    while input_usuario != ' ':
        try:
            input_usuario = input('>> ')            
        except EOFError:
            print('Saliendo...')
            sys.exit(0)
        except KeyboardInterrupt: 
            print('Saliendo...')
            sys.exit(0)
        else:
            print(asistente.responder(input_usuario))

if __name__ == "__main__":
    chatBot()