import hashlib

ssid_prefix = 'Likson-'
salt = 'likson'
password_length = 8
salt_encode = 'ascii'

def get_password(router_mac):
  clave = bytes.fromhex(router_mac) + bytes(salt, salt_encode)  
  _hash = hashlib.sha1(clave).hexdigest()
  password = _hash[-password_length:]
  return password

def get_ssid(router_mac):
  return f'{ssid_prefix}{router_mac[-4:]}'

def print_output(router_mac, ssid, password):
  mac = router_mac.lower()
  print(f'<{mac}> <{ssid}> <{password}>')
  print()

def main():
  print()
  print('Press Ctrl+C to exit')
  print()
  try:
    while True:
      router_mac = input('Dirección MAC del router: ')
      password = get_password(router_mac)
      ssid = get_ssid(router_mac)
      print_output(router_mac, ssid, password) 
  except KeyboardInterrupt:
    print('Bye!')
  

if __name__ == '__main__':
  main()