from functions import get_txt, get_from_card, date_form, mask_card_number

operations_list = get_txt()
my_list = []


def main():
    num_index = 1
    while len(my_list) < 5:
        if operations_list[-num_index]['state'] == 'EXECUTED':
            my_list.append(operations_list[-num_index])
            num_index += 1
        elif operations_list[-num_index]['state'] == 'CANCELED':
            num_index += 1

    for i in my_list:
        date = date_form(i['date'])
        if 'from' in i:
            from_card = get_from_card(i['from'])
            to_card = get_from_card(i['to'])
            mask_to_card = mask_card_number(to_card[-1])
            mask_from_card = mask_card_number(from_card[-1])
            print(f'{date} {i['description']}\n'
                  f'{' '.join(from_card[:-1])} {mask_from_card} -> '
                  f'{' '.join(to_card[:-1])} {mask_to_card}\n'
                  f'{i['operationAmount']['amount']} '
                  f'{i['operationAmount']['currency']['name']}\n')
        elif 'from' not in my_list:
            to_card = get_from_card(i['to'])
            mask_to_card = mask_card_number(to_card[-1])
            print(f'{date} {i['description']}\n'
                  f'{' '.join(to_card[:-1])} {mask_to_card}\n'
                  f'{i['operationAmount']['amount']} '
                  f'{i['operationAmount']['currency']['name']}\n')


if __name__ == '__main__':
    main()
