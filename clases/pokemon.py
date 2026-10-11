class Pokemon:
    contador = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.contador += 1

        print(f"¡{self.nombre} ha sido capturado! ")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado ")

    def entrenar(self, *estadisticas):
        self.nivel += 1

        if len(estadisticas) == 0:
            estadisticas = ("ataque", "defensa", "salud")

        for estadistica in estadisticas:
            if estadistica == "ataque":
                self.ataque += 5
            elif estadistica == "defensa":
                self.defensa += 3
            elif estadistica == "salud":
                self.salud += 10
            else:
                print(f"Estadística no válida: {estadistica}")

        print(f"¡{self.nombre} subió al nivel {self.nivel}!")

    def mostrar_info(self):
        print("\n--- INFORMACIÓN DEL POKÉMON ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar porque está debilitado.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya está debilitado.")
            return

        dano = max(1, self.ataque - objetivo.defensa)

        objetivo.salud = max(0, objetivo.salud - dano)

        print(f"\n¡{self.nombre} atacó a {objetivo.nombre}!")
        print(f"Daño causado: {dano}")
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        print(f"Total de Pokémon creados: {cls.contador}")
        return cls.contador
    