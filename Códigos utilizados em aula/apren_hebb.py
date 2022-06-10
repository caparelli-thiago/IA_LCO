def aprend_hebb(amostras):
     print(f'{"INPUT":^8} {"TARGET":^16}{"VAR. PESOS":^15}{"PESOS":^25}')
     w1, w2, b = 0, 0, 0
     print(' ' * 45, f'({w1:2}, {w2:2}, {b:2})')
     for x1, x2, y in amostras:
         w1 = w1 + x1 * y
         w2 = w2 + x2 * y
         b = b + y
         print(f'({x1:2}, {x2:2})        {y:2}        ({x1*y:2}, {x2*y:2}, {y:2})        ({w1:2}, {w2:2}, {b:2})')


AND_samples = {
    'entrada_binaria_saida_binaria': [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    'entrada_binaria_saida_bipolar': [
        [1, 1, 1],
        [1, 0, -1],
        [0, 1, -1],
        [0, 0, -1]
    ],
    'entrada_bipolar_saida_bipolar': [
        [ 1, 1, 1],
        [ 1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1]
    ]
}
OR_samples = {
    'entrada_binaria_saida_binaria': [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ],
    'entrada_binaria_saida_bipolar': [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, -1]
    ],
    'entrada_bipolar_saida_bipolar': [
        [ 1, 1, 1],
        [ 1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1]
    ]
}
XOR_samples = {
    'entrada_binaria_saida_binaria': [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ],
    'entrada_binaria_saida_bipolar': [
        [1, 1, -1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, -1]
    ],
    'entrada_bipolar_saida_bipolar': [
        [ 1, 1, -1],
        [ 1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1]
    ]
}


print('-'*20, 'HEBBIAN LEARNING', '-'*20)
print('AND com Entrada Binária e Saída Binária')
aprend_hebb(AND_samples['entrada_binaria_saida_binaria'])
print()
print('AND com Entrada Binária e Saída Bipolar')
aprend_hebb(AND_samples['entrada_binaria_saida_bipolar'])
print()
print('AND com Entrada Bipolar e Saída Bipolar')
aprend_hebb(AND_samples['entrada_bipolar_saida_bipolar'])
print()
print()

input()

print(f'-'*20, 'HEBBIAN LEARNING', '-'*20)
print('OR com Entrada Binária e Saída Binária')
aprend_hebb(OR_samples['entrada_binaria_saida_binaria'])
print()
print('OR com Entrada Binária e Saída Bipolar')
aprend_hebb(OR_samples['entrada_binaria_saida_bipolar'])
print()
print('OR com Entrada Bipolar e Saída Bipolar')
aprend_hebb(OR_samples['entrada_bipolar_saida_bipolar'])
print()
print()

input()

print(f'-'*20, 'HEBBIAN LEARNING', '-'*20)
print('XOR com Entrada Binária e Saída Binária')
aprend_hebb(XOR_samples['entrada_binaria_saida_binaria'])
print()
print('XOR com Entrada Binária e Saída Bipolar')
aprend_hebb(XOR_samples['entrada_binaria_saida_bipolar'])
print()
print('XOR com Entrada Bipolar e Saída Bipolar')
aprend_hebb(XOR_samples['entrada_bipolar_saida_bipolar'])


