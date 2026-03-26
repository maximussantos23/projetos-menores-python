class Carro:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.motor = self.Motor()

  class Motor:
    def __init__(self):
      self.status = "Off"

    def ligar(self):
      self.status = "Andando"
      print("Motor ligado")

    def desligar(self):
      self.status = "Off"
      print("Motor desligado")

  def dirigir(self)
    if self.motor.status == "Andando":
      print(f"Dirigindo o {self.marca} {self.modelo}")
    else:
      print("Ligue o motor primeiro!")

carro = Carro("Honda", "Civic")
carro.dirigir()
carro.motor.ligar()
carro.dirigir()
carro.motor.desligar()
carro.dirigir()
