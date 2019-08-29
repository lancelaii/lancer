from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import argparse;

ROOT_DIR = 'websites'

def gather_info(url, quiet=False):
    print( "Gathering info from '{}'.".format( url ) );
    domain_name = get_domain_name( url, quiet );
    ip_address = get_ip_address( domain_name, quiet );
    nmap = get_nmap( '-F', ip_address, quiet );
    robots_txt = get_robots_txt( url, quiet );
    whois = get_whois( domain_name, quiet );

    data = {
            'domain_name':domain_name, 'ip_address':ip_address, 'nmap':nmap,
            'robots_txt':robots_txt, 'whois':whois,
    };

    create_report( data, quiet );

def create_report( data, quiet ):
    project_dir = '{0}/{1}'.format( ROOT_DIR, data['domain_name'] );
    create_dir( project_dir, quiet );
    
    print( "Saving report in '{}'.".format( project_dir ) );

    for key, value in data.items():
        file = '{0}/{1}.txt'.format( project_dir, key );
    

        if not quiet:
            print( 'Saving {}'.format( file ) );
                                     
        write_file( file, value, quiet );

    print( "Done with '{}'.\n".format( data['domain_name'] ) );    

def Main():
    create_dir( ROOT_DIR );

    parser = argparse.ArgumentParser();

    parser.add_argument('url or url_list', help='E.g. http://facebook.com', type=str );
    parser.add_argument('-l', '--list', help='E.g. url_list.txt', action='store_true' );
    parser.add_argument('-q', '--quiet', help='silent mode.', action='store_true' );

    args = parser.parse_args();

    if args.url_list and not args.list:
        gather_info( args.url_list, args.quiet );

    elif args.url_list and args.list:
        print( "Loading website list '{}'".format( args.url_list ) );

        with open( args.url_list, 'r' ) as file:
            data = file.read().split('\n')[:-1];

            for line in data:
                gather_info( line, args.quiet );

        print( "Done with website list '{}'.\n".format( args.url_list ) );

if __name__ == '__main__':
    Main();
