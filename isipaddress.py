def is_ipv4_address(ip):
    """ Return True if ipv4 address, False if not"""
    octets=ip.split('.')
    if len(octets) !=4:
        print ('no son 4 octetos')
        return False
    elif any(not octets.isdigit() for octets in octets):
        resultado='no son digitos'
        print(resultado)
        return False
    elif any(int(octets) < 0 for octets in octets):
        print ('hay menores a cero')
        return False
    elif any(int(octets) > 255 for octets in octets):
        print ('hay mayores a 255')
        return False

    print("ta chingona")
    return True

