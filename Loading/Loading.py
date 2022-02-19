'''
    CASO VA ULTILIZAR EM PROGRAMAS PARA ESPERAR PROCESSAMENTO .. BASTA ALTERAR O TEMPO DE ESPERA
'''
print('''





                        MUITO OBRIGADO POR CONHECER MEU PROGRAMA!
                        Use a vontade...



''')
#--------------------------------Codigo----------------------------------------
from time import sleep

contagem = ''
espacamento = '                                        '  
print('CARREGANDO...')
for c in range(40):
    for i in range(10):
        print(f'\r[ {contagem}{i}{espacamento[:-c - 1]}]',end='')
        if i == 9:
            contagem = '#' + contagem
        #--------------------------Aqui voce define a espera no sleep--------------------------------------
        sleep(0.05)
        #--------------------------------------------------------------------------------------------------

    if c == 39:
        print(f'\r[ {"#" * 40} ]')

#==============================================================================================================
print('Este foi o codigo da barra de carregamento .. obrigado por usar !')