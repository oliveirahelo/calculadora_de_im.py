nome_do_paciente = input("escreva o nome do paciente")
peso = float(input("Digite o peso do paciente"))
altura = float(input("Digite sua altura"))

imc =peso/ (altura*altura)
if imc < 18.5:
    print("abaixo do peso ")
elif imc >= 18.5 and peso <= 24.9:
    print("peso normal")
elif imc >= 25.0 and peso <= 29.9:
    print("sobrepeeso")  
elif imc >= 30.0 and peso <= 34.9: 
    print("obesidade grau I")
elif imc >= 35.0 and peso <= 39.0:
    print("obesidade grau II")    
else:
  print("obesidade grau III")
  