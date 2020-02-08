import os

def locate_ip(url, verbose=False):
    if verbose:
        print( "Getting IP Address from '{}'.".format( url ) )

    action = os.popen( 'host {}'.format( url ) )
    outcome = str( action.read() )
    mark_down = outcome.find( 'has address' ) + 12
    return outcome[mark_down:].splitlines()[0]

#print(locate_ip('aezypay.com'))
