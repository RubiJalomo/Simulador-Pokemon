from clases.pokemon import Pokemon

POKEMONS = []

def capturar_pokemon():
    print("\n--- CAPTURAR POKÉMON ---")

    nombre = input("Nombre: ")
    tipo = input("Tipo: ")

    try:
        ataque = int(input("Ataque inicial: "))
        defensa = int(input("Defensa inicial: "))
        salud = int(input("Salud inicial: "))

        if ataque <= 0 or defensa < 0 or salud <= 0:
            print("El ataque y la salud deben ser positivos.")
            print("La defensa no puede ser negativa.")
            return

        # Crear el objeto y guardarlo en la lista
        nuevo_pokemon = Pokemon(
            nombre, tipo, ataque, defensa, salud
        )

        POKEMONS.append(nuevo_pokemon)

    except ValueError:
        print("Error: debes ingresar números enteros.")


def seleccionar_pokemon():
    if len(POKEMONS) == 0:
        print("No hay Pokémon capturados.")
        return None

    for i, pokemon in enumerate(POKEMONS):
        print(f"{i + 1}. {pokemon.nombre} (Nivel {pokemon.nivel})")

    try:
        opcion = int(input("Selecciona un Pokémon: "))

        if 1 <= opcion <= len(POKEMONS):
            return POKEMONS[opcion - 1]

        print("Opción no válida.")

    except ValueError:
        print("Debes ingresar un número entero.")

    return None


def entrenar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    print("\n¿Qué deseas mejorar?")
    print("1. Todas las estadísticas")
    print("2. Ataque")
    print("3. Defensa")
    print("4. Salud")
    print("5. Ataque y defensa")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pokemon.entrenar()
    elif opcion == "2":
        pokemon.entrenar("ataque")
    elif opcion == "3":
        pokemon.entrenar("defensa")
    elif opcion == "4":
        pokemon.entrenar("salud")
    elif opcion == "5":
        pokemon.entrenar("ataque", "defensa")
    else:
        print("Opción no válida.")


def mostrar_pokemons():
    if len(POKEMONS) == 0:
        print("No hay Pokémon capturados.")
        return

    for pokemon in POKEMONS:
        pokemon.mostrar_info()


def calcular_poder():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    poder = pokemon.ataque + pokemon.defensa + pokemon.salud

    print(f"\nPoder total de {pokemon.nombre}: {poder}")


def combatir():
    print("\nSelecciona tu Pokémon atacante:")
    atacante = seleccionar_pokemon()

    if atacante is None:
        return

    print("\nSelecciona el Pokémon objetivo:")
    objetivo = seleccionar_pokemon()

    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokémon no puede atacarse a sí mismo.")
        return

    atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    POKEMONS.remove(pokemon)

    print(f"{pokemon.nombre} ya no está en tu equipo.")

    del pokemon


def main():
    while True:
        print("\n===== SIMULADOR POKÉMON =====")
        print("1. Capturar Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Ver información de todos")
        print("4. Consultar cantidad de Pokémon")
        print("5. Liberar Pokémon")
        print("6. Calcular poder total")
        print("7. Atacar a otro Pokémon")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_pokemons()
        elif opcion == "4":
            print(f"Pokémon en tu equipo: {len(POKEMONS)}")
            Pokemon.total_pokemons()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            calcular_poder()
        elif opcion == "7":
            combatir()
        elif opcion == "8":
            print("¡Gracias por jugar, entrenador Pokémon!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
