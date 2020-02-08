from tld import get_fld

def get_domain(url, verbose=False):
    if verbose:
        print("Getting Domain Name, '{}'.".format(url));
    
    return get_fld(url)

#print(get_domain('www.aezypay.com'))
