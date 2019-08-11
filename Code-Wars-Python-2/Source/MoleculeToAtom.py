def elements_to_dic(e):
    """ Elements to a dictionary
    :param e: elements in a form of string, and without brackets
    :return: a dictionary with {element_name: num_atoms}
    """
    elements_dic = {}
    initialFound = False
    elemStr = ""
    elemNum = "0"

    for c in e + "-":
        if c.isupper() and not initialFound:
            elemStr += c
            initialFound = True
            continue
        elif c.islower() and initialFound:
            elemStr += c
            continue
        elif c.isdigit():
            elemNum += c
            continue
        elif c.isupper() and initialFound or c == "-":
            # remove leading zero if len is > 1
            if len(elemNum) > 1:
                elemNum = elemNum.lstrip("0")
            elif len(elemNum) == 1:
                elemNum = "1"
            elements_dic[elemStr] = int(elemNum)
            elemStr = c
            elemNum = "0"

    return elements_dic

def mul_molecule(e, mul):
    for key in e:
        e[key] = e[key] * mul
    return e

def find_brackets_multipliers(formula):
    brackets = []
    multipliers = []

    for i in range(len(formula)-1):
        if formula[i] == "}":
            brackets.append(formula[i])
            if formula[i+1].isdigit():
                multipliers.append(int(formula[i+1]))
            else:
                multipliers.append(0)
        elif formula[i] == ")":
            brackets.append(formula[i])
            if formula[i+1].isdigit():
                multipliers.append(int(formula[i+1]))
            else:
                multipliers.append(0)
        elif formula[i] == "]":
            brackets.append(formula[i])
            if formula[i+1].isdigit():
                multipliers.append(int(formula[i+1]))
            else:
                multipliers.append(0)
    print(brackets, multipliers)


def parse_molecule (formula):
    tempDic = elements_to_dic(formula)
    tempDic = mul_molecule(tempDic, 2)
    print(tempDic)
    # figure out the brackets order
    find_brackets_multipliers(formula)
    # find formula in between brackets
    # iterate

#print(elements_to_dic("Mg3Oee72O5Ph"))
#parse_molecule("Mg3Oee72O5Ph")
parse_molecule("K4[ON(SO3)2]2")