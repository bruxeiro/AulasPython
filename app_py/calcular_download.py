from datetime import date, time, datetime, timedelta
#var de entrada

download = float(input('Digite os gebas: '))
velocidade = float(input('Digite a velocidade em mebas: '))

#converte em mb
download_mb = download*1024
print('Você vai baixar: ' + str(download_mb)+ ' mbs')

#print(download_mb)

#converte em segundos
segundos = int(download_mb/velocidade)

#converte em minutos
minutos = segundos/60

#converte em horas
horas = minutos/60



#mostra segundos, minutos e horas necessárias
print ('O dowload vai demorar:  '+ str(segundos) + ' segundos'
        '\nCerca de:  '+ str(minutos) + ' minutos' 
        '\nEm horas:  '+ str(horas) + ' horas'                               
        '\n \nHorário estimado: ')

hora_now = datetime.now()

nova_data = hora_now + timedelta(minutes=int(minutos))

print(nova_data)

#sai do programa
sair = str(input('\nAperte Enter para sair '))