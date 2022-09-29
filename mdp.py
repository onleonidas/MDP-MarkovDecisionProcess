def exchange_value(vetor_reward, up_matriz, dw_matriz, rg_matriz, lf_matriz, value, gamma):

    aux = [[0, 0], [0, 0], [0, 0]]
    pointer = 0
    
    for j in range(2):
        aux[0][j] = value[pointer+2]
        aux[1][j] = value[pointer+1]
        aux[2][j] = value[pointer]
        pointer += 3

    #aux_value = [0, 0, 0, 0, 0, 0]

    for j in range(6):

        up_value, dw_value, lf_value, rg_value = 0, 0, 0, 0
        
        for i in range(6):
            up_value += up_matriz[j][i] * value[i]
            dw_value += dw_matriz[j][i] * value[i]
            rg_value += rg_matriz[j][i] * value[i]
            lf_value += lf_matriz[j][i] * value[i]

        # Equação de Bellman
        value[j] = vetor_reward[j] + gamma * max(up_value, dw_value, lf_value, rg_value)

    for j in aux:
        print(f'{round(j[0], 2)} {round(j[1], 2)}')

    return value


#Função que calcula e printa a política
def return_policy(up_matriz, dw_matriz, rg_matriz, lf_matriz, value):
    policy = []

    for j in range(6):

        up_value, dw_value, lf_value, rg_value = 0, 0, 0, 0

        if j != 2 and j != 5:
            for i in range(6):
                #Calculando as utilidades de um determinado estado s
                up_value += up_matriz[j][i] * value[i]
                dw_value += dw_matriz[j][i] * value[i]
                rg_value += rg_matriz[j][i] * value[i]
                lf_value += lf_matriz[j][i] * value[i]

            moviments = {up_value: 'UP', dw_value: 'DW', rg_value: 'RG', lf_value: 'LF'}
            #O próximo estado s' será o máximo valor das utilidades calculadas acima
            next_moviment = max(up_value, dw_value, lf_value, rg_value)
            #O próximo estado é incluído no array de política
            policy.append(moviments[next_moviment])
        else:
            if j == 2:
                policy.append(-1)
            else:
                policy.append(1)

    #Pritando o array de política
    print(f'| {policy[2]} | {policy[5]}  |')
    print(f'| {policy[1]} | {policy[4]} |')
    print(f'| {policy[0]} | {policy[3]} |')


#Matrizes de probabilidade de transição
rg_matriz = [[0.1, 0.1, 0, 0.8, 0, 0],
            [0.1, 0, 0.1, 0, 0.8, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0.9, 0.1, 0],
            [0, 0, 0, 0.1, 0.8, 0.1],
            [0, 0, 0, 0, 0, 0]]

up_matriz = [[0.1, 0.8, 0, 0.1, 0, 0],
            [0, 0.1, 0.8, 0, 0.1, 0],
            [0, 0, 0, 0, 0, 0],
            [0.1, 0, 0, 0.1, 0.8, 0],
            [0, 0.1, 0, 0, 0.1, 0.8],
            [0, 0, 0, 0, 0, 0]]

lf_matriz = [[0.9, 0.1, 0, 0, 0, 0],
            [0.1, 0.8, 0.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0.8, 0, 0, 0.1, 0.1, 0],
            [0, 0.8, 0, 0.1, 0, 0.1],
            [0, 0, 0, 0, 0, 0]]

dw_matriz = [[0.9, 0, 0, 0.1, 0, 0],
              [0.8, 0.1, 0, 0, 0.1, 0],
              [0, 0, 0, 0, 0, 0],
              [0.1, 0, 0, 0.9, 0, 0],
              [0, 0.1, 0, 0.8, 0.1, 0],
              [0, 0, 0, 0, 0, 0]]


#Bloco principal
reward = -0.04
vetor_reward = [reward, reward, -1, reward, reward, 1]
gamma = 1

value = [0, 0, -1, 0, 0, 1]

for i in range(200):
    print(f'{i + 1}º Iteração')
    value = exchange_value(vetor_reward, up_matriz, dw_matriz, rg_matriz, lf_matriz, value, gamma)
    print('_____________\n')

print('Policy:\n')
return_policy(up_matriz, dw_matriz, rg_matriz, lf_matriz, value)
