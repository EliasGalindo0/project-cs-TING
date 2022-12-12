def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines = data["linhas_do_arquivo"]
        occur = []
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                occur.append(index + 1)
        if len(occur):
            result.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [{"linha": line} for line in occur]
            })

    return result


def search_by_word(word, instance):
    result = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines = data["linhas_do_arquivo"]
        occur = []
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                occur.append({
                  "linha": index + 1,
                  "conteudo": lines[index]
                })
        if len(occur):
            result.append({
              "palavra": word,
              "arquivo": data["nome_do_arquivo"],
              "ocorrencias": occur
            })

    return result
