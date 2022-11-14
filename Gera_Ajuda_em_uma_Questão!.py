import random
def gera_ajuda(dicq):
    l=[]
    for perg, solu in dicq['opcoes'].items():
        if perg!=dicq['correta']:
            l.append(solu)
    rand=random.randint(1,2)
    m=random.sample(l, rand)
    dicq='DICA:\n'
    dicq += 'Opções certamente erradas:' + ' | '.join(m)
    return dicq