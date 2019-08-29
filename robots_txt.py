import urllib.request
import io

def get_robots_txt(url, quiet=False):
    if not quiet:
        print( "Downloading 'robot.txt' from '{}'".format( url ) );

    if not url.endswith( '/' ):
        url += '/';
    request = urllib.request.urlopen( '{}robots.txt'.format( url ), data=None);
    data = io.TextIOWrapper( request, encoding='utf-8' );
    return data.read()

#print(get_robots_txt('https://www.google.com'))
