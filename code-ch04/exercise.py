from ecc import *
from subprocess import *
from helper import *

#========== ex 3
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
Sg = Signature(r,s)

sg_byte = Sg.der()
ans = "3045022037206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c60221008ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec"
# print(sg_byte.hex())
# print(hex(int.from_bytes(sg_byte,'big',signed=False)))
# print(ans)

# ========== ex 5
# pr1 = PrivateKey(100)
# print(pr1.point.address(compressed=False,testnet=True))
# pr2 = PrivateKey(2020**5)
# print(pr2.point.address(compressed=True, testnet=True))
# pr3 = PrivateKey(0x12345deadbeef)
# print(pr3.point.address(compressed=True, testnet=False))

# ========== ex 5

pw = PrivateKey(5003)
print(pw.wif(True,True))