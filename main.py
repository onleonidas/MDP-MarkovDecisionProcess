from matrices import *
from mdp_functions import *

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
