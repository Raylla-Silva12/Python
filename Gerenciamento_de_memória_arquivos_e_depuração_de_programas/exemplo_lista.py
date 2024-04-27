def Lista(time):
    primeiro_indice = time[0]
    ultimo_indice = time[-1]
    time[0], time[-1] = ultimo_indice, primeiro_indice
    print(time)

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
Lista(time)


# Primeiro índice [0] 
# Penúltimo índice [-2]
# Último índice [-1] 



