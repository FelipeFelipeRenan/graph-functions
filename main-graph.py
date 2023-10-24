from collections import deque
import heapq


class Grafo:
    def __init__(self, nome, n, m):
        self.nome = nome
        self.n = n
        self.m = m
        self.adjacencias = {}
    
    @classmethod
    def NovoGrafo(cls):
        novo_grafo = cls("G", 1, 0)
        return novo_grafo

    def EVertice(self, v):
        return v in self.adjacencias


    def AddAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            self.adicionar_aresta(vi, vj, peso)
            self.m += 1
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")


    def RemoveAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            if (vj, peso) in self.adjacencias[vi]:
                self.adjacencias[vi].remove((vj, peso))
                self.m -= 1
            else:
                print(f"A aresta entre {vi} e {vj} com peso {peso} não existe.")
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")


    def ExisteAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            for aresta in self.adjacencias[vi]:
                if aresta[0] == vj and aresta[1] == peso:
                    return True
        return False
    

    def MudaPeso(self, vi, vj, peso_original, novo_peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            arestas_vi = self.adjacencias[vi]
            for i in range(len(arestas_vi)):
                if arestas_vi[i][0] == vj and arestas_vi[i][1] == peso_original:
                    arestas_vi[i] = (vj, novo_peso)
                    return
            print(f"A aresta entre {vi} e {vj} com peso {peso_original} não foi encontrada.")
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")

        
    def ImprimeGrafo(self):
        print("Vértices:")
        for u in self.adjacencias:
            print(f"Vértice {u}")
        
        print("Arestas:")
        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                print(f"Aresta ({u}, {v}) - Peso: {peso}")
    
    
    def RecuperaPeso(self, vi, vj):
        if vi in self.adjacencias and vj in self.adjacencias:
            pesos = []
            for aresta in self.adjacencias[vi]:
                if aresta[0] == vj:
                    pesos.append(aresta[1])
            return pesos
        else:
            print(f"Vi ou Vj não pertencem ao grafo, ou não há arestas entre eles.")
            return []

    def GrafoSimples(self):
        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                if u == v:
                    return False  # O grafo não é simples se houver laços
                for w, _ in self.adjacencias.get(v, []):
                    if w == u:
                        return False  # O grafo não é simples se houver arestas paralelas
        return True  # O grafo é simples
    
    def EArvore(self):
        n = self.n
        m = self.m

        if m != n - 1:
            # Um grafo não é uma árvore se o número de arestas não for igual a n-1
            return False

        # Vamos usar uma busca em profundidade (DFS) para verificar se há ciclos
        visitados = set()
        pilha = [(1, None)]  # Começamos a busca do vértice 1
        arestas_visitadas = set()  # Conjunto para rastrear arestas visitadas

        while pilha:
            v, pai = pilha.pop()
            if v in visitados:
                return False  # Ciclo detectado
            visitados.add(v)

            for u, peso in self.adjacencias.get(v, []):
                if u != pai:  # Evitamos voltar para o pai na busca
                    pilha.append((u, v))
                    arestas_visitadas.add((v, u))

        # Verifica se todas as arestas foram visitadas
        return len(arestas_visitadas) == n - 1
    

    
    def EBipartido(self):
        if self.n == 0:
            return False  # Um grafo vazio não é bipartido

        # Usaremos uma coloração de vértices com duas cores: 0 e 1
        coloracao = {}  # Dicionário para armazenar as cores dos vértices
        visitados = set()  # Conjunto de vértices visitados durante a busca em largura

        for v in self.adjacencias.keys():
            if v not in visitados:
                queue = [v]
                coloracao[v] = 0  # Começamos com a cor 0

                while queue:
                    u = queue.pop(0)
                    visitados.add(u)

                    for w, peso in self.adjacencias.get(u, []):
                        if w not in visitados:
                            queue.append(w)
                            coloracao[w] = 1 - coloracao[u]  # Alternando a cor entre 0 e 1

                        # Verificamos se existe uma aresta entre vértices com a mesma cor
                        if coloracao[w] == coloracao[u]:
                            return False  # O grafo não é bipartido

        return True  # O grafo é bipartido
    

    def Complemento(self):
        grafo_complementar = Grafo(self.nome + "_complementar", self.n, 0)
        
        # Adiciona todos os vértices do grafo original ao grafo complementar
        for u in self.adjacencias:
            grafo_complementar.adicionar_aresta(u, u, 0)  # Adiciona laços no grafo complementar
            for v in self.adjacencias:
                if u != v and (v, 0) not in self.adjacencias[u]:
                    # Se não existe uma aresta entre u e v em G, adicionamos uma no grafo complementar
                    grafo_complementar.adicionar_aresta(u, v, 0)

        return grafo_complementar


    def EAdj(self, vi, vj):
        if vi in self.adjacencias:
            for u, peso in self.adjacencias[vi]:
                if u == vj:
                    return True
        return False
    

    def Adjacencia(self, v):
        if v in self.adjacencias:
            return self.adjacencias[v]
        else:
            print(f"Vértice {v} não pertence ao grafo.")
            return []
        

    def Incidencia(self, v):
        if v in self.adjacencias:
            arestas_incidentes = []
            for u, peso in self.adjacencias[v]:
                arestas_incidentes.append((v, u, peso))
            for u, vizinhos in self.adjacencias.items():
                if u != v:
                    for w, peso in vizinhos:
                        if w == v:
                            arestas_incidentes.append((u, v, peso))
            return arestas_incidentes
        else:
            print(f"Vértice {v} não pertence ao grafo.")
            return []
        
    
    def MatrizAdj(self):
        n = self.n
        matriz_adj = [[float('inf')] * n for _ in range(n)]  # Inicializa a matriz com infinito

        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                matriz_adj[u - 1][v - 1] = peso  # -1 para ajustar ao índice base 0

        return matriz_adj

    def ImprimeMatrizAdj(self):
        matriz_adjacencia = self.MatrizAdj()
        print("Matriz de Adjacência:")
        for linha in matriz_adjacencia:
            print(linha)

    
    def Conexo(self):
        n = self.n
        if n == 0:
            return False  # Um grafo vazio não é conexo

        visitados = set()
        v_inicial = next(iter(self.adjacencias))  # Escolhe um vértice inicial

        def dfs(v):
            visitados.add(v)
            for u, peso in self.adjacencias.get(v, []):
                if u not in visitados:
                    dfs(u)

        dfs(v_inicial)

        return len(visitados) == n  # Se todos os vértices foram visitados, o grafo é conexo


    def RemoveGrafo(self):
        self.nome = ""
        self.n = 0
        self.m = 0
        self.adjacencias = {}
    

    def DFS(self, vi):
        n = self.n
        if vi not in self.adjacencias:
            print(f"O vértice {vi} não pertence ao grafo.")
            return

        visitados = set()
        arvore_de_busca = [-1] * n  # Inicializa o vetor de árvore de busca com -1

        def dfs(v, pai):
            visitados.add(v)
            arvore_de_busca[v - 1] = pai  # -1 para ajustar ao índice base 0

            for u, peso in self.adjacencias.get(v, []):
                if u not in visitados:
                    dfs(u, v)

        dfs(vi, vi)

        print("Árvore de Busca:")
        for i, pai in enumerate(arvore_de_busca):
            print(f"Vértice {i + 1} foi alcançado a partir do vértice {pai}")
        
    
    def BFS(self, vi):
        n = self.n
        if vi not in self.adjacencias:
            print(f"O vértice {vi} não pertence ao grafo.")
            return

        visitados = set()
        arvore_de_busca = [-1] * n  # Inicializa o vetor de árvore de busca com -1

        fila = deque()
        fila.append(vi)
        visitados.add(vi)

        while fila:
            v = fila.popleft()

            for u, peso in self.adjacencias.get(v, []):
                if u not in visitados:
                    fila.append(u)
                    visitados.add(u)
                    arvore_de_busca[u - 1] = v  # -1 para ajustar ao índice base 0

        print("Árvore de Busca (BFS):")
        for i, pai in enumerate(arvore_de_busca):
            print(f"Vértice {i + 1} foi alcançado a partir do vértice {pai}")
    
    
    
    def CaminhoMinimo(self, vi, vj):
        if vi not in self.adjacencias or vj not in self.adjacencias:
            print("Vértices de origem e/ou destino não pertencem ao grafo.")
            return None

        distancias = {v: float('inf') for v in self.adjacencias}
        distancias[vi] = 0

        # Usamos uma fila de prioridade (min heap) para manter os vértices a serem explorados
        fila = [(0, vi)]

        # Dicionário para armazenar os predecessores de cada vértice no caminho mínimo
        predecessores = {v: None for v in self.adjacencias}

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            if vertice_atual == vj:
                caminho = []
                while vertice_atual is not None:
                    caminho.insert(0, vertice_atual)
                    vertice_atual = predecessores[vertice_atual]
                return caminho

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.adjacencias.get(vertice_atual, []):
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, vizinho))
                    predecessores[vizinho] = vertice_atual

        return None  # Não há caminho entre vi e vj


    
    def CustoMinimo(self, vi):
        if vi not in self.adjacencias:
            print(f"O vértice {vi} não pertence ao grafo.")
            return None

        distancias = {v: float('inf') for v in self.adjacencias}
        distancias[vi] = 0

        # Usamos uma fila de prioridade (min heap) para manter os vértices a serem explorados
        fila = [(0, vi)]

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.adjacencias.get(vertice_atual, []):
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return distancias


    def CaminhoMinimo(self, vi):
        if vi not in self.adjacencias:
            print(f"O vértice {vi} não pertence ao grafo.")
            return None

        distancias = {v: float('inf') for v in self.adjacencias}
        distancias[vi] = 0

        # Usamos uma fila de prioridade (min heap) para manter os vértices a serem explorados
        fila = [(0, vi)]

        predecessores = {v: None for v in self.adjacencias}

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.adjacencias.get(vertice_atual, []):
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, vizinho))
                    predecessores[vizinho] = vertice_atual

        caminhos_minimos = {}

        for v in self.adjacencias:
            if v != vi:
                caminho = []
                while v is not None:
                    caminho.insert(0, v)
                    v = predecessores[v]
                caminhos_minimos[v] = caminho

        return caminhos_minimos
    
    def adicionar_aresta(self, u, v, peso):
        if u not in self.adjacencias:
            self.adjacencias[u] = []
        self.adjacencias[u].append((v, peso))

    
    def ler_grafo_do_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

            # Lê a primeira linha para obter o nome, número de vértices e número de arestas
            nome, n, m = linhas[0].strip().split()
            self.nome = nome
            self.n = int(n)
            self.m = int(m)

            # Processa as linhas seguintes para ler as arestas
            for linha in linhas[2:]:
                u, v, peso = linha.strip().split()
                u = int(u)
                v = int(v)
                peso = float(peso)  # Converte o peso para float
                self.adicionar_aresta(u, v, peso)


    def mostrar_grafo(self):
        print(f"Nome do grafo: {self.nome}")
        print(f"Número de vértices: {self.n}")
        print(f"Número de arestas: {self.m}")
        print("Arestas:")
        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                print(f"({u}, {v}) - Peso: {peso}")
    
    
    def mostrar_lista_de_adjacencias(self):
        print("Lista de Adjacências:")
        for u, vizinhos in self.adjacencias.items():
            print(f"Vértice {u} -> {', '.join([f'({v}, {peso})' for v, peso in vizinhos])}")


if __name__ == "__main__":
    nome_arquivo = "graph.txt"  # Substitua pelo nome do arquivo de entrada
    grafo = Grafo("", 0, 0)
    grafo.ler_grafo_do_arquivo(nome_arquivo)
    grafo.mostrar_grafo()
    grafo.mostrar_lista_de_adjacencias()

    # Novo grafo vazio
    novo_grafo = Grafo.NovoGrafo()
    print("\nGrafo Novo:")
    novo_grafo.mostrar_grafo()
    novo_grafo.mostrar_lista_de_adjacencias()

    # Exemplo de uso da função EVertice
    v = 55
    if grafo.EVertice(v):
        print(f"O vértice {v} pertence ao grafo.")
    else:
        print(f"O vértice {v} não pertence ao grafo.")