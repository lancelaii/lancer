import urllib.request
import io

def find_robots(url, verbose=False):
    if verbose:
        print( "Downloading 'Robots.txt' from '{}'".format( url ) );

    if not url.endswith( '/' ):
        url += '/';
    get = urllib.request.urlopen( '{}robots.txt'.format( url ), data=None);
    info = io.TextIOWrapper( get, encoding='utf-8' );
    return info.read()

#print(find_robots('http://aezypay.com'))
