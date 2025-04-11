import pickle # Importa o módulo para serialização e desserialização binária.
import os 
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

# Passageiro (Vagão de passageiros): Comprimento de 22 m a 26 m; 30 a 50 toneladas de peso total [vagão mais passageiros]; até 50 passageiros. 
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

# Carga (Vagão de carga): Comprimento de 12 m a 19 m; de 15 a 30 toneladas de peso total [vagão mais carga]; considerar 75% do peso total do vagão como sendo carga para fins de cálculo. 
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

class Except(Exception):
    """Tratamento de exceção. Uso: em raise Except(<mensagem>)."""
    pass
class Deque:
    def __init__ (self,N):
        """Cria novo deque como lista de tamanho fixo        '''''''-: vetor estático."""
        self._N=N # Tamanho máximo do deque.
        self._data=[None]*N # Lista de tamanho máximo N.
        self._size=0 # Tamanho corrente do deque.
        # Frente (início) do deque: é decrementado/incrementado a cada
        # addFirst()/deleteFirst(), respectivamente.
        self._front=0 # Posição inicial da frente/início.
        # Top (final) do deque: é incrementado/decrementado a cada
        # addLast()/deleteLast(), respectivamente.
        self._top=0 # Posição corrente do topo/fim.
        # Ponteiro utilizado para percorrer o deque.
        self._ptr=0 # Posição do ponteiro no deque (0 no início).
    def isEmpty(self):
        """Retorna verdadeiro se o deque estiver vazio."""
        return self._size==0
    def isFull(self):
        """Retorna verdadeiro se o deque estiver cheio."""
        return self._size==self._N
    def getSize(self):
        """Retorna o tamanho no deque."""
        return self._size
    def peek(self):
        """ Retorna None se o deque estiver vazio.
        Se não, retorna elemento no início do deque sem removê-lo."""
        if self.isEmpty( ):
            return None
        return self._data[self._front] # Primeiro item do deque.
    def top(self):
        """ Retorna None se o deque estiver vazio.
        Senão, retorna elemento no fim do deque sem removê-lo."""
        if self.isEmpty( ):
            return None
        else:
            return self._data[self._top] # Último item do deque.
    def __str__(self):
        """Se o deque estiver vazio,
        retorna mensagem "Deque vazio";
        senão,
        monta uma lista temporária,
        define tamanho da lista temporária como zero,
        coloca o ponteiro livre no início do deque,
        percorre o deque até o final e
        adiciona cada elemento do deque na lista temporária,
        usa str(lista_temp) para retornar o string do deque."""
        if self.isEmpty( ):
            return "Deque vazio."
        else:
            lista_temp=[]
            strSize=0
            self.rewind()
            while strSize<self._size:
                lista_temp.append(self.next())
                strSize+=1
            return str(lista_temp)
    def getVC(self):
        """ Retorna a string do vetor circular (str(lista)) """
        return str(self._data)
    def rewind(self):
        """Coloca ponteiro no início do deque."""
        self._ptr=self._front
    def next(self):
        """Se lista vazia,
        retorna None;
        senão,
        guarda o elemento no ponteiro,
        avança o ponteiro uma posição, circulando se necessário,
        Retorna o elemento guardado."""
        if self.isEmpty():
            return None
        else:
            e=self._data[self._ptr]
            self._ptr+=1
            if self._ptr==self._N: # Passou o fim da deque?
                self._ptr=0 # Circula.
            return e
    def addFirst(self,e):
        """Se deque cheio,
        lança exceção com mensagem.
        Se deque vazio,
        inicializa início (posição 0) com elemento,
        senão,
        decrementa o ponteiro para o início, circulando se necessário;
        adiciona elemento no novo início do deque.
        Aumenta o tamanho do deque."""
        if self.isFull():
            raise Except("Deque cheio!")
        if self.isEmpty():
            self._data[self._front]=e
        else:
            self._front-=1
            if self._front==-1: # Passou o início do vetor?
                self._front=self._N-1 # Circula.
            self._data[self._front]=e
        self._size+=1 # Item adicionado no fim do vetor.
    def addLast(self,e):
        """Se deque cheio,
        lança exceção com mensagem.
        Se deque vazio,
        inicializa início (posição 0) com e.
        senão,
        incrementa o ponteiro para o topo, circulando se necessário,
        adiciona elemento no novo topo do deque.
        Aumenta o tamanho do deque."""
        if self.isFull():
            raise Except("Deque cheio!")
        if self.isEmpty():
            self._data[self._front]=e
        else:
            self._top+=1
            if self._top==self._N: # Passou o fim do vetor?
                self._top=0 # Circula.
            self._data[self._top]=e # Item adicionado no topo/fim do deque.
        self._size+=1

    def deleteFirst(self):
        """Se deque vazio,
        lança exceção com mensagem,
        senão,
        guarda o elemento do início do deque,
        atribui None para a posição corrente do incício,
        diminui o tamanho do deque,
        incrementa a o ponteiro para o início, circulando se necessário,
        retorna o elemento guardado."""
        if self.isEmpty( ):
            raise Except('Deque cheio!')
        else:
            e_front=self._data[self._front] # Primeiro do deque.
            self._data[self._front]=None # Limpa posição.
            self._size-=1
            self._front+=1
            if self._front==self._N: # Passou o fim do vetor?
                self._front=0 # Circula.
            return e_front
    def deleteLast(self):
        """Se deque vazio,
        lança exceção com mensagem,
        senão,
        guarda o elemento do topo do deque,
        atribui None para a posição corrento do topo,
        diminui o tamanho do deque,
        decrementa a o ponteiro para o topo, circulando se necessário,
        retorna o elemento guardado."""
        if self.isEmpty( ):
            raise Except('Deque vazio!')
        else:
            e_top=self._data[self._top] # Último do deque.
            self._data[self._top]=None # Limpa posição.
            self._size-=1
            self._top-=1
            if self._top==-1: # Passou o início do vetor?
                self._top=self._N-1 # Circula.
            return e_top
class Persistente:
    def __init__(self, nome_arquivo):
 # Construtor da classe Persistente.
 # Recebe o nome do arquivo onde os dados serão armazenados.
 # O atributo é protegido (_nome_arquivo), acessível por subclasses.
        self._nome_arquivo = nome_arquivo
    def salvar(self, dados):
 # Método que salva os dados fornecidos no arquivo especificado.
 # Os dados podem ser listas, dicionários, objetos ou outros tipos
 # serializáveis com pickle. 
        try:
 # Abre o arquivo no modo binário de escrita ('wb').
            with open(self._nome_arquivo, 'wb') as arq:
                # Serializa os dados e grava no arquivo.
                pickle.dump(dados, arq)
            # Informa que os dados foram salvos com sucesso.
            print("Dados salvos em: " + self._nome_arquivo)
        except (pickle.PicklingError, PermissionError, OSError) as e:
            # Em caso de erro na serialização ou permissão, exibe a mensagem.
            print("Erro ao salvar arquivo '" + self._nome_arquivo + "':", e)
    def carregar(self):
        # Método que tenta carregar os dados de um arquivo, se ele existir.
        # Retorna os dados desserializados. Em caso de erro, retorna lista vazia.
        if os.path.exists(self._nome_arquivo):
        # Se o arquivo existir, tenta carregá-lo.
            try:
                # Abre o arquivo no modo binário de leitura ('rb').
                with open(self._nome_arquivo, 'rb') as arq:
                    # Desserializa os dados do arquivo.
                    dados = pickle.load(arq)
        # Informa que o carregamento foi realizado com sucesso.
                print("Arquivo '" + self._nome_arquivo +
                "' carregado com sucesso.")
                return dados # Retorna os dados carregados.
            except (pickle.UnpicklingError, EOFError,PermissionError, OSError) as e:
        # Em caso de erro na leitura, exibe a mensagem e retorna lista vazia.
                print("Erro ao carregar arquivo '" + self._nome_arquivo + "':", e)
                return []
        else:
        # Se o arquivo não existir, informa e retorna lista vazia.
            print("Aviso: Arquivo '" + self._nome_arquivo +
            "' não encontrado.")
            return []
        
class ComposicaoFerroviaria(Deque, Persistente):
    def __init__(self, N, nome_arquivo):
    # Inicializa o deque e o mecanismo de persistência.
        Deque.__init__(self, N)
        Persistente.__init__(self, nome_arquivo)
        self.carregar() # Carrega dados do arquivo, se existir.
        # Usa método carregar sobrecarregado.

    # Contabiliza a carga transportada pela composição.
    def contar_carga_total(self):
        total_carga = 0
        for vagao in self._data: # Itera em todos os vagões (self._data herdado de Deque).
            if isinstance(vagao, Carga): # Se for vagão de carga
                total_carga += vagao.carga # contabiliza a carga (75% do peso)
        return total_carga
    
    def criar_composicao_padrao(self):
        # Apaga composição anterior: reinicializa a Composição Ferroviária (Deque).
        self._data = [None] * self._N
        self._size = 0
        self._front = 0
        self._top = 0
        # Cria a composição padrão.
            #< Repetições utilizando métodos de adição, conforme anexo >
        try:
            # Adiciona locomotivas
            self.addLast(Locomotiva(comprimento=20, peso=150, potencia=2500))

            # Adiciona vagões de passageiros
            for i in range(50):
                self.addLast(Passageiro(comprimento=24, peso=40, num_passageiros=30))

            # Adiciona vagões de carga
            for i in range (30):
                self.addLast(Carga(comprimento=17, peso=20))
            
            # Salva a composição no arquivo
            self.salvar()
            print("Composição padrão criada e salva com sucesso.")
        except Except as e:
            print(f"Erro ao criar composição padrão: {e}")
    
    def salvar(self):
        # Salva a composição inteira no arquivo usando método herdado.
        Persistente.salvar(self, self)
    def carregar(self):
        # Carrega a composição do arquivo, se disponível.
        dados = Persistente.carregar(self)
        # Atualização dos dados da composição na memória (em uso).
        # O tamanho do vetor (_N) é assumido o mesmo.
        # Atualiza se dados não for None (arquivo não encontrado).
        if isinstance(dados, ComposicaoFerroviaria):
            self._data = dados._data
            self._size = dados._size
            self._front = dados._front
            self._top = dados._top

    def inserir_vagao(self, op):
        print("\n----- Tipos de vagões disponíveis -----")
        print("1 - Locomotiva")
        print("2 - Vagão de Passageiros")
        print("3 - Vagão de Carga")
        tipo = input_int("\nSelecione o tipo de vagão: ", 1, 3)
        
        try:
            if tipo == 1:  # Locomotiva
                comprimento = input_float("Comprimento entre 18 e 23 metros: ", 18, 23)
                peso = input_float("Peso entre 100 e 200 toneladas: ", 100, 200)
                potencia = input_float("Potência entre 2000 e 6000 HP: ", 2000, 6000)
                vagao = Locomotiva(comprimento, peso, potencia)
            elif tipo == 2:  # Passageiro
                comprimento = input_float("Comprimento entre 22 e 26 metros: ", 22, 26)
                peso = input_float("Peso entre 30 e 50 toneladas: ", 30, 50)
                num_passageiros = input_int("Número de passageiros entre 0 e 50: ", 0, 50)
                vagao = Passageiro(comprimento, peso, num_passageiros)
            elif tipo == 3:  # Carga
                comprimento = input_float("Comprimento entre 12 e 19 metros: ", 12, 19)
                peso = input_float("Peso entre 15 e 30 toneladas: ", 15, 30)
                vagao = Carga(comprimento, peso)
            
            if op == 1:
                self.addFirst(vagao)
            elif op == 2: 
                self.addLast(vagao)
            else:
                raise Except("Opção de inserção errada")
            
            self.salvar()
            print("Vagão inserido com sucesso!")
        except Except as e:
            print(f"Erro: {e}")

    def remover_vagao(self, op):
        if op == 1:
            self.deleteFirst()
        elif op == 2: 
            self.deleteLast()
        else:
            raise Exception("Opção de remoção errada")
        
        self.salvar()
    
    def quant_vagoes(self):
        qtd_locomitiva = 0
        qtd_passageiro = 0
        qtd_carga = 0
        qtd_vagao = 0
        for vagao in self._data:
            if isinstance(vagao, Locomotiva):
                qtd_locomitiva += 1
            elif isinstance(vagao, Passageiro):
                qtd_passageiro += 1
            elif isinstance(vagao, Carga):
                qtd_carga += 1
            qtd_vagao += 1
    
        return qtd_locomitiva, qtd_passageiro, qtd_carga, qtd_vagao

    def comprimento_vagoes(self):
        comprimento = 0
        for vagoes in self._data:
            if isinstance(vagoes,Vagao):
                comprimento += vagoes.comprimento
                comprimento += 2
        comprimento -= 2
        return comprimento
    
    def carga_e_passageiro(self):
        carga = 0 
        Passageiros = 0
        for vagoes in self._data:
            if isinstance(vagoes,Carga):
                carga += vagoes.carga 
            elif isinstance(vagoes,Passageiro):
                Passageiros += vagoes.num_passageiros
        return carga, Passageiros
    
    def verificar_potencia(self):
        peso_total = 0
        potencia_total = 0
        qtd_locomotivas = 0

        # Calcula o peso total e a potência total das locomotivas
        for vagao in self._data:
            if isinstance(vagao, Vagao):
                peso_total += vagao.peso
            if isinstance(vagao, Locomotiva):
                potencia_total += vagao.potencia
                qtd_locomotivas += 1

        # Verifica a relação potência/peso
        if peso_total == 0:
            return "A composição está vazia. Não há peso para verificar."

        relacao_potencia_peso = potencia_total / peso_total

        # Define o limite mínimo de potência/peso (ajuste conforme necessário)
        limite_minimo = 1.05  # Exemplo: 0.1 HP por tonelada

        if relacao_potencia_peso >= limite_minimo:
            return f"A potência é suficiente. Relação potência/peso: {relacao_potencia_peso:.2f} HP/tonelada."
        else:
            # Calcula a potência necessária e sugere locomotivas adicionais
            potencia_necessaria = (limite_minimo * peso_total) - potencia_total
            if qtd_locomotivas > 0:
                potencia_por_locomotiva = potencia_total / qtd_locomotivas
                locomotivas_adicionais = -(-potencia_necessaria // potencia_por_locomotiva)  # Arredonda para cima
                return (f"A potência é insuficiente. Relação potência/peso: {relacao_potencia_peso:.2f} HP/tonelada.\n"
                        f"Faltam {potencia_necessaria:.2f} HP. Adicione aproximadamente {int(locomotivas_adicionais)} "
                        f"locomotiva(s) igual(is) às já incluídas.")
            else:
                return "A composição não possui locomotivas. Adicione pelo menos uma locomotiva."
            
    def diagnostico_composicao(self):
        # Obtém os resultados dos métodos
        qtd_locomotivas, qtd_passageiros, qtd_cargas, qtd_total = self.quant_vagoes()
        comprimento_total = self.comprimento_vagoes()
        carga_total, passageiros_total = self.carga_e_passageiro()
        potencia_diagnostico = self.verificar_potencia()

        # Monta o diagnóstico
        diagnostico = (
            "-------- Diagnóstico da Composição Ferroviária --------\n\n"
            f"- Quantidade de vagões:\n"
            f"  Locomotivas: {qtd_locomotivas}\n"
            f"  Passageiros: {qtd_passageiros}\n"
            f"  Cargas: {qtd_cargas}\n"
            f"  Total: {qtd_total}\n"
            f"- Comprimento total dos vagões: {comprimento_total} metros\n"
            f"- Carga total transportada: {carga_total:.2f} toneladas\n"
            f"- Total de passageiros: {passageiros_total}\n"
            f"\n- Diagnóstico de potência:\n{potencia_diagnostico}\n\n"
        )

        return diagnostico
    
    def Imprime_primeiro(self):
        """Imprime o primeiro elemento do deque."""
        if self.isEmpty():
            print("Deque vazio.")
        else:
            print("Primeiro elemento:")
            self.peek().imprime()
    def Imprime_ultimo(self):
        """Imprime o último elemento do deque."""
        if self.isEmpty():
            print("Deque vazio.")
        else:
            print("Último elemento:")
            self.top().imprime()

# Função para ler um número inteiro dentro da faixa esperada dada pelo professor
def input_int(msg, inf, sup):
    while True:
        entrada = input(msg)
        if entrada.lstrip('-').isdigit():
            n = int(entrada)
            if inf <= n <= sup:
                return n
        print(f"Erro. Digite um valor entre {inf} e {sup}")

# Função para ler um número real dentro da faixa esperada dada pelo professor
def input_float(msg, inf, sup):
    while True:
        s = input(msg)
        s = s.replace(',', '.')
        eh_numero = True
        tem_ponto = 0
        for c in s:
            if c == '.':
                tem_ponto += 1
            elif not c.isdigit():
                eh_numero = False
        if tem_ponto > 1:
            eh_numero = False
        if eh_numero and s != '':
            n = float(s)
            if inf <= n <= sup:
                return n
        print(f"Erro. Digite um valor entre {inf} e {sup}")

def opcoes():
    print("--------- Composição Ferroviária ---------\n")
    print("1 - criar composição padrão")
    print("2 - inserir vagão")
    print("3 - remover vagão")
    print("4 - apresentar a descrição da composição")
    print("5 - apresentar os dados do primeiro vagão")
    print("6 - apresentar os dados do último vagão")
    print("7 - terminar\n")
    
def principal():
    try:
        composicaoferroviaria = ComposicaoFerroviaria(100, "composicao.pkl")
        while True:
            opcoes()
            escolha = input_int("Selecione sua opção: ", 1, 7)
            if escolha == 1:
                composicaoferroviaria.criar_composicao_padrao()
            elif escolha == 2:
                op = input_int("Digite 1 para inserir no início ou 2 para inserir no final: ", 1, 2)
                composicaoferroviaria.inserir_vagao(op)
            elif escolha == 3:
                op = input_int("Digite 1 para remover do início ou 2 para remover do final: ", 1, 2)
                composicaoferroviaria.remover_vagao(op)
            elif escolha == 4:
                print(composicaoferroviaria.diagnostico_composicao())
            elif escolha == 5:
                composicaoferroviaria.Imprime_primeiro()
            elif escolha == 6:
                composicaoferroviaria.Imprime_ultimo()  
            elif escolha == 7:
                break
            else:
                print("Escolha inválida! Selecione uma opção de 1 a 7")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    principal()
