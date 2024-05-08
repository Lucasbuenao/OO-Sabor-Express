from modelos.avaliacao import Avaliacao

class Restaurante():
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        # Use a função __init__() para atribuir valores a propriedades de objeto ou outras operações que são necessárias fazer quando o objeto está sendo criado. / Sintaxe: def __init__(self,...):

        self._nome = nome.title()
        # .title() = Deixa a primeira letra da palavra em maiúsculo;

        self._categoria = categoria.upper()
        # .upper() = Deixa todas letras em MAIÚSCULO;

        self._ativo = False
        Restaurante.restaurantes.append(self)
        # append() = O método acrescenta um elemento ao final da lista.

        self._avaliacao = []
        # foi criado como lista, pois será necessário ter a capacidade de receber várias avaliações.

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        # mostra o objeto em formato de texto -> __srt__;
        # Sintaxe: def __srt__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    # @classmethod = Retorna um método de classe para uma determinada função.
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    # @property = serve para modificar a forma que o atributo será lido.
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✔️' if self._ativo else '❌' 
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
