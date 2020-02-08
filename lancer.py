from modules.common import *
from modules.dns import *
from modules.ip import *
from modules.ports import *
from modules.robots import *
from modules.whois import *
import argparse;

ROOT_DIR = 'websites'

def merge_data(url, verbose=False):
    print("----------------------------------------------------------------- \n Started lancer scanner for '{}'.".format(url),"\n-----------------------------------------------------------------\n")
    dns = get_domain(url, verbose)
    ip = locate_ip(dns, verbose)
    ports = get_ports('-sV', ip, verbose)
    robots = find_robots(url, verbose)
    whois = find_whois(dns, verbose)

    info = {
            'dns':dns, 'ip':ip, 'ports':ports,
            'robots':robots, 'whois':whois,
    };

    make_report(info, verbose)


def make_report(info, verbose):
    project_dir = '{0}/{1}'.format(ROOT_DIR, info['dns'])
    make_dir(project_dir, verbose)
    
    print("Saving report to '{}'.".format(project_dir))

    for key, value in info.items():
        data = '{0}/{1}.html'.format(project_dir, key)
    

        if verbose:
            print( 'Saving {}'.format(data))
                                     
        record_docs(data, value, verbose)

    print( "Done with '{}'.\n".format( info['dns'] ) ) 


def ALL():
    make_dir(ROOT_DIR)

    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='E.g. https://www.google.com', type=str)
    parser.add_argument('-l', '--list', help='E.g. url_list.txt', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbose mode.', action='store_true')

    args = parser.parse_args()

    if args.url and not args.list:
        merge_data(args.url, args.verbose)

    elif args.url and args.list:
        print( "Loading website list '{}'".format(args.url))

        with open( args.url, 'r' ) as data:
            info = data.read().split('\n')[:-1]

            for line in info:
                merge_data(line, args.verbose)

        print( "Done with website list '{}'.\n".format(args.url))


if __name__ == '__main__':
    ALL()
