from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=50)  
    direccion = models.CharField(max_length=300) 
    contacto = models.CharField(max_length=50)  
    nombre_contacto = models.CharField(max_length=50)  
    fecha_ingreso = models.DateField()  
    razon_social = models.CharField(max_length=300)  
    direccion_fiscal = models.CharField(max_length=300) 
    rut = models.CharField(max_length=300) #Averiguar si lleva un maximo de longitud
    mail = models.EmailField()
    cronograma = models.TextField()

class Obra(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=300)
    metros_cuadrados = models.DecimalField(max_digits=10, decimal_places=3)
    recaudo_grafico = models.ImageField(upload_to='imagenes/')
    # Cuando se guarden las imagenes se guardaran en un directorio llamado imagenes
    cliente = models.ForeignKey(Cliente, related_name='obras', on_delete=models.CASCADE) # relacion con tabla cliente
                # para acceder a todas las obras de cada cliente se usa cliente.obras.all()
                # CASCADE hace que si se elimina un cliente tambien se eliminen todas sus obras relacionadas 

class PuntoLimpio(models.Model):
    ubicacion = models.CharField(max_length=300)  
    metros = models.DecimalField(max_digits=10, decimal_places=2) 
    estructura = models.CharField(max_length=300)
    tipo_contenedor = models.CharField(max_length=300) 
    estado_contenedor = models.CharField(max_length=300)  
    senaletica = models.BooleanField() 
    observaciones = models.TextField() 
    obra = models.ForeignKey(Obra, related_name='puntolimpio', on_delete=models.CASCADE)  # Relación con Obra
    # Igual que la relacion anterior uno a muchos, se puede acceder a todos los puntos limpios de una obra desde el modelo Obra usando obra.puntos_limpios.all()

class Materiales(models.Model):
    estado = models.CharField(max_length=300) 
    proteccion = models.CharField(max_length=300) 
    tipo = models.CharField(max_length=300)
    punto_limpio = models.ForeignKey(PuntoLimpio, related_name='materiales', on_delete=models.CASCADE) #relacion con punto limpio

class SupervisorDeObra(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    Email = models.EmailField()
    obra = models.OneToOneField(Obra, on_delete=models.SET_NULL, null=True)

class Visitas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    motivo = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=300)
    obra = models.ForeignKey(Obra, related_name='visitas', on_delete=models.CASCADE) #DUDA

class Tecnicos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    visitas = models.ForeignKey(Visitas, related_name='tecnicos', on_delete=models.SET_NULL, null=True) #DUDA

class CoordinacionRetiro(models.Model):
    descripcion = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=300)
    estado = models.CharField(max_length=300)
    fecha_solicitud = models.DateField()
    fecha_retiro = models.DateField()
    pesaje = models.IntegerField()
    comentarios = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    obra = models.ForeignKey(Obra, related_name='coordinacionretiro', on_delete=models.CASCADE) #DUDA

class Transportistas(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=20)
    email = models.EmailField()
    tipo_material = models.CharField(max_length=300)
    tipo_vehiculo = models.CharField(max_length=300)
    coordinacionretiro = models.ForeignKey(CoordinacionRetiro, related_name='transportistas', on_delete=models.SET_NULL, null=True) #DUDA

class EmpresaTratamiento(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=300)
    contacto = models.CharField(max_length=50)
    email = models.EmailField()
