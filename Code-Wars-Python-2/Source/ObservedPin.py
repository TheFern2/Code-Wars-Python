from itertools import product

def get_pins(observed):
    a = ['80', '124', '1235', '236', '1457', '24568', '3569', '478', '57890', '689']
    return [''.join(j) for j in product(*(a[int(i)] for i in observed))]