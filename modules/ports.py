import os

def get_ports(options, ip, verbose=False):
    if verbose:
        print( "Starting ports scanning on {}".format( ip ) )

    action = os.popen( "nmap {0} {1}".format( options, ip ) )
    outcome = str( action.read() )
    return outcome

#print(get_ports('', '192.168.31.66'))
