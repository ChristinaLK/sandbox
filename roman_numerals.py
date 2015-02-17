import sys

this_script = sys.argv[0]
input_numerals = sys.argv[1:]

roman_dict = {"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000}

def convert_to_list(rom_str):
    rom_list = []
    for char in rom_str:
        rom_list.append(roman_dict[char])
    rom_list.append(0)
    return rom_list

def list_to_number(rom_list):
    temp = 0
    total = 0
    for i,element in enumerate(rom_list):
        temp = temp + element
        if element == 0:
            total = total+temp
        elif element < rom_list[i+1]:
            total = total - temp
            temp = 0
        elif element > rom_list[i+1]:
            total = total + temp
            temp = 0
    return total


def convert_roman_numerals(rom_str):
    rom_list = convert_to_list(rom_str)
    number = list_to_number(rom_list)
    return number

#convert_roman_numerals("XV")

#convert_roman_numerals("C")

#convert_roman_numerals("XXIV")

#convert_roman_numerals("XLIX")

for item in input_numerals:
    print "Roman Numeral is: "+item
    print "Arabic Numeral is: ", convert_roman_numerals(item)

