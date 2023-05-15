def percentual_exames_alterados(lista, exame, referencia):
    total_exames = 0
    total_alterados = 0
    for elemento in lista:
        if elemento[1] == exame:
            total_exames += 1
            if elemento[3] > referencia:
                total_alterados += 1
    return round(total_alterados*100/total_exames,2) if total_exames > 0 else 0
