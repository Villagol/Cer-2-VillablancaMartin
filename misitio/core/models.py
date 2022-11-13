from django.db import models

# Create your models here.
class Residencia(models.Model):
    numero= models.IntegerField(primary_key=True)
    dueno = models.CharField(max_length=50)
    telefono= models.IntegerField()
    correo= models.CharField(max_length=50)
    def __str__(self) -> str:
        return "Residencia "+str(self.numero)


class Correspondencia(models.Model):
    fecha_recepcion= models.DateField()
    conserje= models.CharField(max_length=50)
    remitente= models.CharField(max_length=50)
    destinatario= models.CharField(max_length=50)
    estados=(
            ("Seleccione","Seleccione"),
            ("Recibido","Recibido"),
            ("No Recibido","No recibido") )
    estado=models.CharField(max_length=20, choices=estados, default="S")
    nroresidencia= models.ForeignKey(Residencia, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "Correspondencia para "+str(self.destinatario)+", "+str(self.nroresidencia)