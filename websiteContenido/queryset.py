from django.db import models

'''
Esta clase va a obtener todas los contenidos de distintas paginas
'''


class WebsiteContenidoQuerySet(models.QuerySet):
    def pagina(self, pagina):
        return self.get(pagina=pagina).texto
