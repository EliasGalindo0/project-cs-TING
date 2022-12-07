import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            print('Formato inválido', file=sys.stderr)

        with open(path_file) as file:
            data = file.read()
            txt_file = [text_line for text_line in data.split('\n')]
            print(txt_file)
            return txt_file
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
