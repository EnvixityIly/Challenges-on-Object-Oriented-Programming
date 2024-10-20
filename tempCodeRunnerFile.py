class py_solution:
    def int_to_roman(self,num):
        val = [1000,900,500,500,100,90,50,50,10,9,5,4]
        syb = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_num = ''
        while num > 0:
            for i in range(num//val(i)):
                roman_num += syb[i]
                num -= val[i]
            i += 1
            return roman_num
print(py_solution().int_to_roman(1))
print(py_solution().int_to_roman(35))
print(py_solution().int_to_roman(650))
print(py_solution().int_to_roman(1254))
