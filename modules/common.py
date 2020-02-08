import os

def make_dir(directory, verbose=False):
    if not os.path.exists( directory ):
        if verbose:
            print( "Creating new directory, '{}'.".format( directory ) );

        os.makedirs( directory );

    else:
        if verbose:
            print( "Directory already exists, '{}'.".format( directory ) );


def record_docs(path, data, verbose=False):
    if verbose:
        print( "Writing '{}'.".format( path ) );

    with open(path, 'w') as file:
        file.write( data );



#print(make_dir('common'))
#file = 'common/hi.txt'.format()
#value = ""
#print(record_docs(file, value))
