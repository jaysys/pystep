#

import sys
import module.mod_01 as person
import module.mod_02 as dan
import module.mod_03 as calc


print(sys.version)
print

a = person.human("Joo", 45)
a.hello()
a.info()

dan.gugu()

print(calc.add(2,3.0))
print(calc.subtract(2.0,3))
print(calc.multiply(2,3.0))
print(calc.divide(2.0,3.0))

print("BYE")





