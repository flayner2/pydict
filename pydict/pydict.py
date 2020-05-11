from fuzzywuzzy import fuzz
from utils.parsers import read_csv

data = read_csv('./data/dict.csv')

print('Bem vindx ao PyDict! Digite uma palavra em inglês e aperte ENTER para buscar seu significado.')
print('DICA: digite GETOUT (em caixa alta) ou use ctrl+c pra sair.\n')

while(True):

    match = False

    user_entry = input('Sua busca: ')

    if user_entry == 'GETOUT':
        break

    try:
        print(f'{", ".join(data[user_entry])}\n')
    except (KeyError):
        for valid_word in list(data):
            if fuzz.token_sort_ratio(valid_word, user_entry) >= 80:
                print(
                    f'Ops, palavra não encontrada! Você não quis dizer "{valid_word}"?\n')
                match = True
                break
        if not match:
            print('Ops! Palavra não encontrada!\n')
