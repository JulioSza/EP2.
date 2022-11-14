def questao_para_texto(pergunta,id):
    string = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(id,pergunta['titulo'],pergunta['opcoes']['A'],pergunta['opcoes']['B'],pergunta['opcoes']['C'],pergunta['opcoes']['D'])
    return string