def add_amount_to_persons(amount_dict, ids, amount_to_add):
    # function to split an amount with persons, id is the list of ids of the corresponding persons
    per_head = amount_to_add / len(ids)
    for id in ids:
        amount_dict[id] += per_head

