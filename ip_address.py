import os

def get_ip_address(url, quiet=False):
    if not quiet:
        print( "Getting ip address from '{}'.".format( url ) );

    process = os.popen( 'host {}'.format( url ) );
    results = str( process.read() );
    marker = results.find( 'has address' ) + 12;
    return results[marker:].splitlines()[0];

#print(get_ip_address('google.com'))
