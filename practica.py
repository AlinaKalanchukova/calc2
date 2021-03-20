instr = input('Что вычислить?')
print(instr)
instr = instr.replace(' ', '')
print(instr)
supported_ops = tuple('+-*/^')
print(supported_ops)
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
supported_ops = hp_ops +mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

actions = list()
d = dict()
d['opr'] = 'First'
d['val'] = None
actions.append(d)
print(actions)

i = 0
for letter in instr:
   if letter in supported_ops:
     actions.append({'ops': letter, 'val': ''})
     pass # под операции
   elif letter in digit_chars:
     actions[-1]['val'] += letter
     pass # под числа
     
ptint(actions)
