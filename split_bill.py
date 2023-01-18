def add_amount_to_persons(amount_dict, ids, amount_to_add):
    # function to split an amount with persons, id is the list of ids of the corresponding persons
    per_head = amount_to_add / len(ids)
    for id in ids:
        amount_dict[id] += per_head


def app():
    # input persons list, sample input: 'david,john'
    participants = input('Enter participants separated by comma: ')
    participants = participants.strip()

    if not participants:
        print('Please enter valid text, exiting..')
        exit()

    participants = participants.split(',')

    # strip spaces
    participants = [x.strip() for x in participants]

    participant_dict = {}
    participant_ids = []
    amount_dict = {}

    # generating ids for each persons
    for i, name in enumerate(participants):
        participant_dict[i] = name
        participant_ids.append(i)
        amount_dict[i] = 0

    print('\nUse the id from below to add consumed food amount to that person')
    for i, participant_data in participant_dict.items():
        print(f"{participant_data} - {i}")

    # add bill
    total = int(input('\nEnter total bill: '))

    # separate bills
    amount = ''

    # splittable amount
    splitted_amount = 0

    print('\nAdding splittable bills, Enter amount as 0 to stop\n')
    while True:
        amount = int(input('Enter splittable bill: '))
        splitted_amount += amount

        if amount == 0:
            break

        # input persons to split the amount
        ids = input("Enter ids of persons in scope separated by ',' : ")
        ids = ids.split(',')

        # converts it to int
        ids = [int(id.strip()) for id in ids]

        add_amount_to_persons(amount_dict, ids, amount)

        # show remaining amount
        print('Remaining bill: ', total - splitted_amount)

    # add common amount (amount remaining after splittable amounts)
    add_amount_to_persons(amount_dict, participant_ids, total - splitted_amount)

    print('\nSummary\n-------')
    print('Name\tAmount\n------------')

    for key, amount in amount_dict.items():
        print(f"{participant_dict[key]} : \t{amount}")


if __name__ == '__main__':
    app()
