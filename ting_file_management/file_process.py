import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    info = {
      'nome_do_arquivo': path_file,
      'qtd_linhas': len(content),
      'linhas_do_arquivo': content
    }

    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    instance.enqueue(info)
    sys.stdout.write(str(info))


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
        return None
    info = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(f'Arquivo {info} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        sys.stdout.write(f'{instance.search(position)}\n')
    except IndexError:
        sys.stderr.write('Posição inválida\n')
