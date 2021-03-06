"""
CPF = 168.995.350-09
-------------------------------------------------------------------------
1 * 10 = 10            #    1 * 11 = 11
6 * 9  = 54            #    6 * 10 = 60
8 * 8  = 64            #    8 * 9  = 72
9 * 7  = 63            #    9 * 8  = 72
9 * 6  = 54            #    9 * 7  = 63
5 * 5  = 25            #    5 * 6  = 30
3 * 4  = 12            #    3 * 5  = 15
5 * 3  = 15            #    5 * 4  = 20
0 * 2  = 0             #    0 * 3  = 0
                       # -> 0 * 2  = 0
         297           #             343
11 - (297 % 11) = 11   #  11 - (343 % 11) = 9
11 > 9 = 0             #
Digito 1 = 0           #  Digito 2 = 9
"""

while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:9]
    cpf_lista = [novo_cpf]
    reverso = 10
    soma = 0
    for index in range(19):
        if index > 8:
            index -= 9
        # print(cpf[index], index, reverso)
        soma += int(cpf[index])*reverso
        reverso -= 1
        if reverso < 2:
            # print(soma)
            reverso = 11
            d = 11 - (soma % 11)
            if d > 9:
                cpf_lista.append('0')
            else:
                cpf_lista.append(f'{d}')
            mult = 0
            soma = 0
    novo_cpf = ''.join(cpf_lista)
    # print(novo_cpf)
    if novo_cpf == cpf:
        print('CPF válido.')
        break
    else:
        print('CPF inválido.')