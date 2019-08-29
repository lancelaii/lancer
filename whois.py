import os

def get_whois(domain_name, quiet=False):
    if not quiet:
        print( "Getting 'whois' info from '{}'.".format( domain_name ) );

    process = os.popen( 'whois {}'.format( domain_name ) );
    results = str( process.read() );
    return results

#print(get_whois('google.com'))
