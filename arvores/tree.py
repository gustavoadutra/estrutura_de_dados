from queue import Queue

ROOT = "root"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data=None, node=None):
        # cria o objeto arvore
        # se for dado um node ele se torna root
        if node:
            self.root = node
        # se tiver informação se cria um node e ele se torna root
        elif data:
            node = Node(data)
            self.root = node
        # se não o root recebe none
        else:
            self.root = None

    # percurso em ordem simetrica
    def simetric_traversal(self, node=None):
        # se o node for vazio o node se torna o root
        if node is None:
            node = self.root
        # se tiver um valor a esquerda do node ele vai printar e vai buscar mais valores a esquerda
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)

        print(node.data, end='')

        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    # percurso em pós ordem mesma coisa que simétrica
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.data)

    # calculo da altura de determinado nó
    def height(self, node=None):
        # se tiver módulo não vazio o node vai ser o root
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        # se tiver um módulo a esquerda ele continua procurando a esquerda
        # vai até encontrar o último e retorna a altura com o valor hleft + 1
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        # faz a verificação para o último valor e retorna a altura maior que é a válida
        if hright > hleft:
            return hright + 1
        return hleft + 1
    
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            print(node)
            queue.push(node.left)
            # se o valor a esquerda não for nulo
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node.data, end=" ")


class BinarySearchTree(BinaryTree):
    # faz a inserção na arvore 
    def insert(self, value):
        # pai recebe none
        parent = None
        # x é o root
        x = self.root
        # enquanto x ainda retornar um valor vai procurar a posição para fazer a inserção
        while(x):
            # pai se torna o valor acima do xx
            parent = x
            # se o valor dentro do módulo x for maior que o valor para inserir continue seguindo a esquerda
            if value < x.data:
                x = x.left
            else:
                x = x.right

        # se o pai for vazio o root vai se tornar o node com o valor dentro
        if parent is None:
            self.root = Node(value)
        # se o valor do pai for menor que o valor ele se torna um módulo na esquerda
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):
        # se o node estiver zerado o node recebe root
        if node == 0:
            node = self.root
        # se tiver vazio apenas retorna o node
        if node is None:
            return node
        # se encontrar retorna o objeto/módulo
        if node.data == value:
            return BinarySearchTree(node)
        # se o valor for menor ou maior continue procurando com a mesma regra de se for menor para esquerda
        # maior para a direita
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
    
    # percurso em pós ordem mesma coisa que simétrica
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.data)