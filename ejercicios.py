#Ejercicio número 1
class Persona:

  def __init__(self):
    self.nombre=input("Ingrese el nombre: ")
    self.edad=int(input("Ingrese la edad: "))

  def mostrar(self):
    print("Nombre: ",self.nombre)
    print("Edad: ",self.edad)

class Empleado(Persona):

  def __init__(self):

    super().__init__()
    self.sueldo=float(input("Ingrese el sueldo: "))

  def mostrar(self):
    super().mostrar()
    print("Sueldo: ",self.sueldo)

  def pagar_impuestos(self):
    if self.sueldo > 3600000:
      descuento = self.sueldo * 0.035
      total = self.sueldo - descuento
      round(descuento)
      round(total)
      print('El descuento que se le va a hacer tiene un total de:', descuento,'pesos')
      print('El total que debe para es de:', total, 'pesos')
    else:
      print("El empleado no paga impuestos.")

persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()

#Ejercicio número 2
class Alumno:
  def __init__(self):
    self.nombre = input('Digite su nombre: ')
    self.nota = int(input('Digite su nota: '))

  def calificacion(self):
    if self.nota < 3:
      print('Que pelad@ tan menso, tiene que estudiar, que pena')
    if self.nota == 3:
      print('Que chin@ tan de buenas, pasó de chiripa')
    else:
      print('Buena crack, aprobaste, haz que tu gfa se sienta orgullosa, sigue así')

alumno1 = Alumno()
alumno1.calificacion()

#Ejercicio número 3
class matema:
  def __init__(self):
    self.num1 = int(input('Digite el primer numero: '))
    self.num2 = int(input('Digite ek segundo número: '))

  def suma(self):
    suma = self.num1 + self.num2
    print('El resultado que da lasuma de los dos números es: ',suma)

  def multiplicacion(self):
    mul = self.num1 * self.num2
    print('El resultado que da lasuma de los dos números es: ',mul)

  def division(self):
    div = self.num1 / self.num2
    print('El resultado que da lasuma de los dos números es: ',div)

numeros = matema()
numeros.suma()
numeros.multiplicacion()
numeros.division()