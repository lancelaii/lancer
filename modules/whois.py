import os

def find_whois(domain_name, verbose=False):
    if verbose:
        print( "Getting 'Whois' info from '{}'.".format( domain_name ) );

    action = os.popen( 'whois {}'.format( domain_name ) );
    outcome = str(action.read());
    return outcome

#print(find_whois('aezypay.com'))
