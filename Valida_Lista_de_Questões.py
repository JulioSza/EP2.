def valida_questao(pergunta):
    a = {}
    chaves = ['titulo','nivel','opcoes','correta']
    dificuldade = ['facil','medio','dificil']
    opcoes = ['A','B','C','D']
    chaveq = pergunta.keys()
    for c in chaves:
        if c not in chaveq:
            a[str(c)] = 'nao_encontrado'
    if len(pergunta.keys()) != 4:
       a['outro'] = 'numero_chaves_invalido'
    if 'titulo' in chaveq:
        car = list(set(pergunta['titulo']))
        if pergunta['titulo'] == '' or ((' ' in car or '\t' in car)  and len(car) < 3): 
            a['titulo'] = 'vazio'
    if 'nivel' in chaveq:
        if pergunta['nivel'] not in dificuldade:
            a['nivel'] ='valor_errado'
    if 'opcoes' in chaveq:
        opc = pergunta['opcoes'].keys()
        if len(opc) != 4:
            a['opcoes'] = 'tamanho_invalido'
        elif len(opc) == 4:
            itens = set(opc)
            S = True
            for op in opc:
                if op not in opcoes or len(itens) < 4:
                    a['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    S = False
            if S == True and 'opcoes' in chaveq:
                a["opcoes"] = {}
                no = True
                valores = list(pergunta['opcoes'].values())
                print(valores)
                for v in range(len(valores)):
                    car2 = list(set(valores[v]))
                    if valores[v] == '' or ((' ' in car2 or '\t' in car2)  and len(car2) < 3):
                        a['opcoes'][str(opcoes[v])] = 'vazia'
                        no = False
                if no:
                    a.pop("opcoes")
    if 'correta' in chaveq:
        if pergunta['correta'] not in opcoes:
            a['correta'] =  'valor_errado'
    return a


def valida_questoes(listap):
    listar = []
    for q in listap:
        resultado = valida_questao(q)
        listar.append(resultado)

    return listar
