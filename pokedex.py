#----------------------------------------------------------------------
# Base de pokedex
# La base de pokedex representa una lista de todos los pokemon.
#
# Cada pokemon es un diccionario que incluye los siguientes keys (propiedades):
# - pokemon: Nombre para identificar el pokemon
# - num: Numero del pokemon
# - tipo: Lista de posibles tipos del pokemon
# - peso: Peso del pokemon
# - altura: Altura del pokemon
# - debilidad: Lista de posibles tipos a los cuales es debil el pokemon
# - fortaleza: Lista de posibles tipos a los cuales es fuerte el pokemon
# - descripcion: Descripcion del pokemon
#----------------------------------------------------------------------
def pokedexC():
    '''
    Define la base de datos de la pokedex
    rawtype de string
    :return el pokedex a mostrar
    :rtype str 
    '''
    pokedex = [
        #////////////////////////////////////////////////Bulbasaur.
        {
            'pokemon': 'bulbasaur',
            'num': '001',
            'tipo': [
                'planta',
                'veneno'
            ],
            'peso': '6.9 kg',
            'altura': '0.7 m',
            'debilidad': [
                'fuego',
                'volador',
                'hielo',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'planta',
                'tierra',
                'electrico'
            ],  
            'descripcion': 'Bulbasaur es un Pokémon de tipo planta/veneno introducido en la primera generación. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        }
    ]
    return pokedex

def pokemonesC():
    # Lista de los 151 Pokémon originales
    pokemones = [
        "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
        "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
        "metapod", "butterfree", "weedle", "kakuna", "beedrill",
        "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate",
        "spearow", "fearow", "ekans", "arbok", "pikachu",
        "raichu", "sandshrew", "sandslash", "nidoran", "nidorina",
        "nidoqueen", "nidoran", "nidorino", "nidoking", "clefairy",
        "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff",
        "zubat", "golbat", "oddish", "gloom", "vileplume",
        "paras", "parasect", "venonat", "venomoth", "diglett",
        "dugtrio", "meowth", "persian", "psyduck", "golduck",
        "mankey", "primeape", "growlithe", "arcanine", "poliwag",
        "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam",
        "machop", "machoke", "machamp", "bellsprout", "weepinbell",
        "victreebel", "tentacool", "tentacruel", "geodude", "graveler",
        "golem", "ponyta", "rapidash", "slowpoke", "slowbro",
        "magnemite", "magneton", "farfetchd", "doduo", "dodrio",
        "seel", "dewgong", "grimer", "muk", "shellder",
        "cloyster", "gastly", "haunter", "gengar", "onix",
        "drowzee", "hypno", "krabby", "kingler", "voltorb",
        "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
        "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
        "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan",
        "horsea", "seadra", "goldeen", "seaking", "staryu",
        "starmie", "mr-mime", "scyther", "jynx", "electabuzz",
        "magmar", "pinsir", "tauros", "magikarp", "gyarados",
        "lapras", "ditto", "eevee", "vaporeon", "jolteon",
        "flareon", "porygon", "omanyte", "omastar", "kabuto",
        "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
        "moltres", "dratini", "dragonair", "dragonite", "mewtwo",
        "mew"]
    return pokemones