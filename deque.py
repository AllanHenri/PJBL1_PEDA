class Except(Exception):
    """Tratamento de exceção. Uso: em raise Except(<mensagem>)."""
    pass
class Deque:
    def __init__ (self,N):
        """Cria novo deque como lista de tamanho fixo: vetor estático."""
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
