def gf_add(a, b):
  return a ^ b

def gf_multiply(a, b):
  tmp, aes = a, 0
  if b & 0x01:
    res = gf_add(res, tmp)
  while b != 0:
    b >>= 1
    tmp <<= 1
    if b & 0x1:
      res = gf_add(res, tmp)
  
  return res

def gf_xtime(a):
  if a & 0x80:
    return ((a << 1) ^ 0x1b) & 0xff
  else:
    return (a << 1) & 0xff
