import re


def create_csv_from_dic(index_file, dic_file, out_file):
    meanings = {}

    with open(index_file, 'r') as index:
        print('Reading index file...')
        lines = index.readlines()
        word_index = [word.split('\t')[0] for word in lines]

    with open(dic_file, 'r') as dictionary:
        print('Reading dict file and creating temporary dictionary...')
        dict_lines = dictionary.readlines()
        for v_index, vernacle in enumerate(word_index):
            for l_index, line in enumerate(dict_lines[v_index:]):
                if '/' in line and vernacle == re.findall(r'.+?(?= /)', line)[0]:
                    meanings[vernacle] = []
                    for m_index, meaning in enumerate(dict_lines[dict_lines.index(line)+1:]):
                        if '/' not in meaning:
                            meanings[vernacle].append(
                                meaning.strip().replace(',', ';'))
                        else:
                            del dict_lines[l_index+1:m_index+1]
                            break
                    break

    with open(out_file, 'w') as output:
        print('Writing dictionary to output csv file...')
        for entry, translations in meanings.items():
            output.write(
                f'{entry},{",".join(translations)}\n')


def read_csv(csv_file):
    with open(csv_file, 'r') as input_csv:
        print('Reading csv file and creating dictionary...')
        entries = input_csv.read().splitlines()
        return {items.split(',')[0]: items.split(',')[1:] for items in entries}


create_csv_from_dic('./eng-por/eng-por.index',
                    './eng-por/eng-por.dict', './dict.csv')

print(read_csv('./dict.csv'))
