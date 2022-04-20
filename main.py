from palindrom import palindrom
from printOS import get_os
from validatorIP import validate_ip

print(palindrom("nan pap pup, banana d da,aa! pdp,>D: PPkk kppk"))

print(validate_ip("1.1.1.01"))
print(validate_ip("1.1.1.255:0000"))
print(validate_ip("1.1.1.025"))

print(get_os())
