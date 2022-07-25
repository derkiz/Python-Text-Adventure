import random

# Generate 10 NPCs onto a list.

# Names to chose from
names = [
    'Russell Kirk',
    'Peter Wheeler',
    'Hans Moon',
    'Manuela Skinner',
    'Velma Mahoney',
    'Carl Huynh',
    'Kent Miller',
    'Duane Best',
    'Angela Pena',
    'Josef Lucero',
    'Coy Bruce',
    'Margery Vaughan',
    'Chad Mcintosh',
    'Deon Francis',
    'Juana Burch',
    'Thelma Daniel',
    'Christie Lowe',
    'Deangelo Phelps',
    'Glen Swanson',
    'Antone Hayes',
    'Elisabeth James',
    'Carrol Pruitt',
    'Errol Fischer',
    'Noreen Guzman',
    'Rene Mays',
    'Yvette Rodriguez',
    'Noelle Ramos',
    'Nellie Morales',
    'Wesley Daniels',
    'Chang Montes',
    'Sandra Dudley',
    'Bert Pace',
    'Paulette Clay',
    'Leopoldo Galvan',
    'Reed Mcdowell',
    'Martina Donovan',
    'Glenda Arias',
    'Nadine Pearson',
    'Colette Good',
    'Mia Floyd',
    'Millie Tran',
    'Josefa Davenport',
    'Pat Farley',
    'Javon Herring',
    'Ralph Higgins',
    'Gillian Hendrix',
    'Laura Levine',
    'Eileen Chen',
    'Agustin Huang',
    'Kristin Pruitt',
    'Liana Hubbard',
    'Hillary Price',
    'Myla Hubbard',
    'Raelynn Good',
    'Martin Gross',
    'Rebecca Silva',
    'Kade Carson',
    'Vaughn Cain',
    'Maggie Oconnor',
    'Amanda Ray',
    'Karissa Haas',
    'Aron Mccoy',
    'Norah Nash',
    'Mina Perkins',
    'Karter Santana',
    'Savion Brandt',
    'Aleah Shea',
    'Trevor Taylor',
    'Steve Salinas',
    'Sidney Li',
    'Madilyn Spencer',
    'Kasen Garza',
    'Sandra Wall',
    'Kaleb Brennan',
    'Luz Everett',
    'Savannah Wiley',
    'Haven Malone',
    'Antwan Howe',
    'Jazmin Gay',
    'Mohamed Porter',
    'Isiah Fox',
    'Geovanni Meadows',
    'Brody Bentley',
    'Kayley Parsons',
    'Branden Carroll',
    'Kassandra Shaffer',
    'Avah Mitchell',
    'Ashly Travis',
    'Kamari Beck',
    'Jeramiah Acevedo',
    'Lucian Hanna',
    'Baylee Bernard',
    'Aliya Walker',
    'Maren Flowers',
    'Jase Whitehead',
    'Annika Craig',
    'Jacey Keller',
    'Mckayla Horne',
    'Kasey Glass',
    'Colby Ellison',
    'Lorena Petty',
]

# Empty List for Generation Function
gen_list = []


# Random Names into a compiled list
# To change length of list modify the 10 to any positive whole number in while statement
def ran_gen(lists):
    x = 0
    while x != 10:
        x += 1
        # print(x)
        n = (random.randint(0, 99))
        # print(n)
        # print(names[n])
        if (names[n]) in gen_list:
            # print(f'item {names[n]} already found')
            x -= 1
        else:
            gen_list.append(names[n])


ran_gen(1)
# print(gen_list)
