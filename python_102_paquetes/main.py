import pkg
from pkg.mod_1 import saludar,preguntar 
from pkg.mod_2 import adios


if __name__ == '__main__':
    print(pkg.time)
    print(saludar())
    print(preguntar('Daniel'))
    print(adios('Daniel'))
