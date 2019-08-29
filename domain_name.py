from tld import get_fld

def get_domain_name(url, quiet=False):
    if not quiet:
        print( "Getting domain name,'{}'.".format( url ) );
    
    return get_fld( url );

#print(get_domain_name('https://www.google.com'))
