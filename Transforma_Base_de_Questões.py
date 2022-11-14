def transforma_base(pergunta):
    dicio = {}
    l_f = []
    l_m = []
    l_d = []
    
    for p in pergunta:
        for p, d in p.items():
            if d == 'facil':
                l_f.append(p)

            elif d == 'medio':
                l_m.append(p)
            
            elif d == 'dificil':
                l_d.append(p)
         
    if len(l_f) != 0:
        dicio['facil'] = l_f

    if len(l_m) != 0: 
        dicio['medio'] = l_m
    
    if len(l_d) != 0:
        dicio['dificil'] = l_d

    return dicio