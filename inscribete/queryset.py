from django.db import models


class InscribeteQueryset(models.QuerySet):

    def porEstudiante(self, estudianteId):
        return self.filter(estudiante__pk=estudianteId)

    def costoTotalPorEstudiante(self, estudianteId):
        pass
