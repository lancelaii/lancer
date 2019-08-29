import os

def get_nmap(options, ip, quiet=False):
    if not quiet:
        print( "Performing 'nmap' scan on {}".format( ip ) );

    process = os.popen( "nmap {0} {1}".format( options, ip ) );
    results = str( process.read() );
    return results;

#print(get_nmap('-F', '192.168.31.67'))
