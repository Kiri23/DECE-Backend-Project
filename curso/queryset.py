from django.db import models
from django.db.models import Q


class CursoQuerySet(models.QuerySet):
    '''
    Esta clase va a tener los querys relacionados solamente con la tabla cursos
    '''

    def porCategorias(self, categorias):
        """
        Devuelve cursos por categorias
        """
        return self.filter(categoria__nombre__in=categorias)

    def porTitulo(self, titulo):
        """
        Devuelve cursos por titulo
        """
        print(f'queryset por titulo: {titulo}')
        # Utilizar el | para utilizar el or
        return self.filter(Q(titulo__icontains=titulo))


class CategoriasQuerySet(models.QuerySet):
    '''
    Esta clase va a tener los querys relacionados solamente con la tabla categorias
    '''

    def masPopulares(self):
        """
        Devuelve las categorias mas populares
        """
        return self.all().order_by('popularidad')[:5]


class TemasQuerySet(models.QuerySet):
    '''
    Esta clase va a tener los querys relacionados con la tabla Temas
    '''

    def porCursoId(self, id):
        """
         Esta función solamente devuelva el nombre del tema   
        """
        return self.filter(curso__pk=id).only('nombre')


class SubtemasQuerySet(models.QuerySet):
    '''
    Esta clase va a tener los querys relacionados con la tabla Subtemas
    '''

    def subtemas(self, temas_id: list, curso_id: int):
        """
        Devuelve todos los subtemas para un teme que pertenezca a un especifico curso. Porque recuerda pueden haber un tema que pertenezca a mas de un curso. 

        Esta funcion solo devuelve el nombre del subtema

        :param temas_id: El id del tema
        :param curso_id: El id del curso    
        """
        try:
            if type(temas_id) is list:
                return self.filter(tema__pk__in=temas_id, tema__curso__pk=curso_id).only('nombre')
        except expression as identifier:
            # TODO: Send error to sentry
            print('Hubo un error al buscar los subtemas para un prontuario. Los id de cada tema tienen que venir en una lista. Alomejor eso pude ser el error.')

# Examples of how to make documentation para que snphix la reconozca https://numpydoc.readthedocs.io/en/latest/example.html#source


class PreviewMaekdown:
    """
    A class used to test al the markdown I can represent in Vscode info view of a class and function. El unico markdown que no funciona es el de Emphasis como bold, underline, dash

    Puedes empezar una nueva linea con \
    hello\  
    world

    - [ ] hacer esto 
    - [ ] hacer lo otro

    - [X] Todo lo demas
    - [ ] Todo

    # H1

    Alt-H1
    ======

    1. First ordered list item
    1. Another item
    1. Another item


    [I'm an inline-style link](https://www.google.com)

    Reference-style: 
    ![alt text][logo]

    [logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

    > Quotes

    Python Code Block
    ```python
    s = "Python syntax highlighting"
    print s
    for name in names:
        name
    ```
    Three or more --- to create a horinzontal rule 

    ---

    Tables 

    Colons can be used to align columns.

    | Tables        | Are           | Cool  |
    | ------------- |:-------------:| -----:|
    | col 3 is      | right-aligned | $1600 |
    | col 2 is      | centered      |   $12 |
    | zebra stripes | are neat      |    $1 |

    There must be at least 3 dashes separating each header cell.

    ---

    [Pagina de donde saque los ejemplos](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
