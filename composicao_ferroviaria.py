'''Tipos de vagões a serem considerados na montagem da composição'''

# Classe base para os vagões
class Vagao:
    def __init__(self, comprimento, peso):
        self.comprimento = comprimento
        self.peso = peso

    def imprime(self):
        print(f"Comprimento: {self.comprimento} m, Peso: {self.peso} toneladas")

# Locomotiva: Comprimento entre 18 m 23 m; 100 a 200 toneladas de peso [quanto mais potência, maior o peso]; potência entre 2000 HP e 6000 HP. 
class Locomotiva(Vagao):
    def __init__(self, comprimento, peso, potencia):
        # Validação do comprimento (18m a 23m)
        if not (18 <= comprimento <= 23):
            raise ValueError("Comprimento da locomotiva deve estar entre 18m e 23m")
        
        # Validação do peso (100t a 200t)
        if not (100 <= peso <= 200):
            raise ValueError("Peso da locomotiva deve estar entre 100t e 200t")
        
        # Validação da potência (2000HP a 6000HP)
        if not (2000 <= potencia <= 6000):
            raise ValueError("Potência da locomotiva deve estar entre 2000HP e 6000HP")
        
        super().__init__(comprimento, peso)
        self.potencia = potencia

    def imprime(self):
        print(f"Tipo: Locomotiva")
        super().imprime()
        print(f"Potência: {self.potencia} HP")

# Passageiro (Vagão de passageiros):Comprimento de 22 m a 26 m; 30 a 50 toneladas de peso total [vagão mais passageiros]; até 50 passageiros. 
class Passageiro(Vagao):
    def __init__(self, comprimento, peso, num_passageiros):
        # Validação do comprimento (22m a 26m)
        if not (22 <= comprimento <= 26):
            raise ValueError("Comprimento do vagão de passageiros deve estar entre 22m e 26m")
        
        # Validação do peso (30t a 50t)
        if not (30 <= peso <= 50):
            raise ValueError("Peso do vagão de passageiros deve estar entre 30t e 50t")
        
        # Validação do número de passageiros (até 50)
        if not (0 <= num_passageiros <= 50):
            raise ValueError("Número de passageiros deve ser entre 0 e 50")
        
        super().__init__(comprimento, peso)
        self.num_passageiros = num_passageiros

    def imprime(self):
        print(f"Tipo: Passageiro")
        super().imprime()
        print(f"Número de passageiros: {self.num_passageiros}")

# Carga (Vagão de carga)Comprimento de 12 m a 19 m; de 15 a 30 toneladas de peso total [vagão mais carga]; considerar 75% do peso total do vagão como sendo carga para fins de cálculo. 
class Carga(Vagao):
    def __init__(self, comprimento, peso):
        # Validação do comprimento (12m a 19m)
        if not (12 <= comprimento <= 19):
            raise ValueError("Comprimento do vagão de carga deve estar entre 12m e 19m")
        
        # Validação do peso (15t a 30t)
        if not (15 <= peso <= 30):
            raise ValueError("Peso do vagão de carga deve estar entre 15t e 30t")
        
        super().__init__(comprimento, peso)
        self.carga = peso * 0.75  # 75% do peso total é carga

    def imprime(self):
        print(f"Tipo: Carga")
        super().imprime()
        print(f"Peso da carga: {self.carga} toneladas") 