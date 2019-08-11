import unittest
from MoleculeToAtom import parse_molecule

def equals_atomically(obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True

class MoleculeTests(unittest.TestCase):
    def test(self):
        self.assertTrue(equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}), "Should parse water")
        self.assertTrue(equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
        self.assertTrue(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")
        self.assertTrue(equals_atomically(parse_molecule("B2H6"), {'B': 2,  'H': 6}))
        self.assertTrue(equals_atomically(parse_molecule("C6H12O6"), {'C': 6,  'H': 12, 'O':6}))
        self.assertTrue(equals_atomically(parse_molecule("(C5H5)Fe(CO)2CH3"), {'C': 6,  'H': 12, 'O':6}))
        self.assertTrue(equals_atomically(parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5"), {'C': 6,  'H': 12, 'O':6}))