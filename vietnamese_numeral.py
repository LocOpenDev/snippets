
vietnamese_numeral_map = (
    (10, 'Muoi'),
    (9, 'Chin'),
    (8, 'Tam'),
    (7, 'Bay'),
    (6, 'Sau'),
    (5, 'Nam'),
    (4, 'Bon'),
    (3, 'Ba'),
    (2, 'Hai'),
    (1, 'Mot'),
    (0, 'Khong')
)

numberlen_unit_map = (
    (5, 'TramNgan', 100000),
    (5, 'MuoiNgan', 10000),
    (4, 'Ngan', 1000),
    (3, 'Tram', 100),
    (2, 'Muoi', 10),
    (1, '', 1),
)

to_vietnamese_table = []
from_vietnamese_table = {}

def build_lookup_tables():
    def lookup_number_unit(n):
        vn_number_unit = ''
        number_unit = 0
        number_len = len(str(n))
        for numlen, vn_num_unit, num_unit in numberlen_unit_map:
            if number_len == numlen:
                vn_number_unit = vn_num_unit
                number_unit = num_unit
                break
        return (vn_number_unit, number_unit)

    def to_vietnamese(n):
        number_len = len(str(n))
        vn_number_unit, number_unit = lookup_number_unit(n)
        
        result = ''
        if number_len > 1:
            while number_unit > 1:
                mode = n % number_unit
                unit = n // number_unit
                if unit > 1:
                    result += to_vietnamese_table[unit] + vn_number_unit
                else:
                    result += vn_number_unit
                n = mode
                vn_number_unit, number_unit = lookup_number_unit(n)
            else:
                n = mode
        if number_len == 1 or number_len > 1 and n > 0:
            for number, vietnamese in vietnamese_numeral_map:
                if n >= number:
                    result += vietnamese
                    n -= number
                    break

            if n > 0:
                result += to_vietnamese_table[n]
        
        return result
    
    for i in range(999999):
        vietnamese_number = to_vietnamese(i)
        to_vietnamese_table.append(vietnamese_number)
        from_vietnamese_table[vietnamese_number] = i

build_lookup_tables()

print(to_vietnamese_table)