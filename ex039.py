peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))
imc = peso / (altura ** 2)
print (f'o imc dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('você esta abaixo do peso ideal!')
elif imc >= 18.5 and imc <= 25:
    print('você esta no peso ideal!')
elif imc >= 25 and imc <= 30:
    print ('você esta em sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('você esta em obesidade!')
else:
    print('você esta em obesidade morbida!')
