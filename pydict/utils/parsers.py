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
                if '/' in line and (re.search(rf'{vernacle} /', line)
                                    or (re.search(rf'{vernacle},', line))
                                    or (re.search(rf', {vernacle},', line))
                                    or (re.search(rf', {vernacle} /', line))):
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
        entries = input_csv.read().splitlines()
        return {items.split(',')[0]: items.split(',')[1:] for items in entries}
