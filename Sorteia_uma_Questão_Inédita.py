import random
def sorteia_questao_inedida(dicq, dificuldade, l):
    qsr=random.choice(dicq[dificuldade])
    l.append(qsr)
    return qsr