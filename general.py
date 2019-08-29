import os

def create_dir(directory, quiet=False):
    if not os.path.exists( directory ):
        if not quiet:
            print( "Creating new directory, '{}'.".format( directory ) );

        os.makedirs( directory );

    else:
        if not quiet:
            print( "Directory already exists, '{}'.".format( directory ) );


def write_file(path, data, quiet=False):
    if not quiet:
        print( "Writing '{}'.".format( path ) );

    with open(path, 'w') as file:
        file.write( data );
