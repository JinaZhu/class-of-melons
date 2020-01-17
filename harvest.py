############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code        


def make_melon_types():
    """Returns a list of current melon types."""

    # Fill in the rest

    musk = MelonType('musk', 1998, 'green',
                     True, True, 'Muskmelon')
    musk.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', True, False, 'Casaba')
    casaba.add_pairing('strawberry')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing('prosciutto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')


    all_melon_types = [musk, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    all_melons = {}

    for melon in melon_types: 
        # all_melons[melon.code] = {'first_harvest': melon.first_harvest, 
        #                           'color': melon.color, 
        #                           'seed': melon.is_seedless, 
        #                           'Bestseller': melon.is_bestseller, 
        #                           'Name': melon.name
        #                           }
        all_melons[melon.code] = melon

    return all_melons


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape, color, field, harvested_by):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        return self.shape > 5 and self.color > 5 and self.field != 3



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)

    melons1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melons2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melons3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melons4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melons5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melons6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melons7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melons8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melons9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    all_melons = [melons1, melons2, melons3, melons4, melons5, melons6,
                  melons7, melons8, melons9]

    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons: 
        if melon.is_sellable():
            print_sellability = "CAN BE SOLD"
        else:
            print_sellability = "NOT SELLABLE"

        # status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'

        print(f"Harvested by {melon.harvested_by} from Field {melon.field} ({print_sellability}).")


def more_melons(file_name, melon_types):
    file = open(file_name)
    melons_by_id = make_melon_type_lookup(melon_types)

    all_harvested_melons = []

    for line in file:
        line = line.rstrip()
        melon_line = line.split()
        # melon_line = ['Shape', '1', 'Color', '2', 'Type', 'yw', 'Harvested', 'By', 'Sheila', 'Field', '#', '37']
        new_melon = Melon(melons_by_id[melon_line[5]],
                          int(melon_line[1]), int(melon_line[3]),
                          int(melon_line[-1]), melon_line[-4])
        all_harvested_melons.append(new_melon)

    return all_harvested_melons


