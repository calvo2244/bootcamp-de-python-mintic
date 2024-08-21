# diccionario siempre en llaves clave:valor

numbers = { 1: "uno", 2:"dos" , 3:"tres"} 
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])

# print(numbers[4])#genera error por que no existe 

information = {"nombre" : "Hector",
               "apellido" : "Astudillo",
               "estatura" : 1.69,
               "cena" : False}
print("diccionario completo ")
print(information)

del information ["apellido"]
print("eliminando " )
print(information)

claves =  information.keys()
print("Mostrando solo las claves " )
print(claves)

values =  information.values()
print("Mostrando solo los valores " )
print(values)

pairs =  information.items()
print("Recorrido por el diccionario " )
print(pairs)

contacts = {
    "Hector": {"Apellido": "Astudillo",
                "Altura":1.71,
                "edad":42,
                "Telefono":3008880519,
                "Signo Zodiacal":"cancer",
                "Pelicula_Favorita":"Silicon Valley",
                "Cancion_Favorita":"Algo que se quede - grupo niche",
                "Comida_Favorita":"Sancocho",
                "Lugar soñado vacaciones":"miami",
                "Habilidad secreta":"xxxxxx",
                "Pasatiempo":"Videojuegos- fc24",
                "Heroe o personaque admiras":"Steve Jobs",
                "LIbro que mas me ha impactado":"xxxxx",
                "Cenar con alguien":"mi esposa jejej",
                "Superpoder":"Rapido aprendizaje",
                "Que logro personla te enorgullese":"Aprender React"
                },
    "Hector":   {"Apellido":"Astudillo", 
                "Altura":1.71,
                "edad":42, 
                "Telefono":3008880519,
                "Signo sodiacal": "cancer",
                "Serie favorita":"Silicon Valley",
                "cancion favorita" :"Algo que se quede - grupo niche",
                "Lugar soñado de vacaiones": "miami",
                "habilidad":"vacio",
                "pasatiempo":"Videojuegos- fc24",
                "Heroe o personas que mas admiras":"Steve Jobs",
                "Libro que mas te ha impactado":"no tengo",
                "cenar con alguien":"mi esposa jejej",
                "superpoderes":"Rapido aprendizaje",
                "logro personal":"Aprender React"
    },
}
    "Aurelio": {"Apellido": "cheveroni",
                "Altura":1.51,
                "edad":15,
                "Telefono":30055555,
                "Signo Zodiacal":"geminis",
                "Pelicula_Favorita":"Silicon Valley",
                "Cancion_Favorita":"Algo que se quede - grupo niche",
                "Comida_Favorita":"Sancocho",
                "Lugar soñado vacaciones":"miami",
                "Habilidad secreta":"xxxxxx",
                "Pasatiempo":"Videojuegos- fc24",
                "Heroe o personaque admiras":"Steve Jobs",
                "LIbro que mas me ha impactado":"xxxxx",
                "Cenar con alguien":"mi esposa jejej",
                "Superpoder":"Rapido aprendizaje",
                "Que logro personla te enorgullese":"Aprender React"
                }    
    }
print("******* todo el diccionario Contacts ********")
print(contacts)