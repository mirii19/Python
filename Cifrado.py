from Crypto.Hash import MD5
m = MD5.new()
m.update('Hola mundo')
print m.digest()
