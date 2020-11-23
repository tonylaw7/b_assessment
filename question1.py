"""
Please write a program that can read the contents of any directory (and its subdirectories) in the
filesystem, and print out the contents sorted in order of file size in the command line. The directory to
search should be passed in as a parameter to the program.
The output should show the full path of the file, the file name, and the file size.
"""
import argparse
import os


def print_list(output_tuples_list):
    """
    Prints the sorted output list of tuples containing the parent_path, filename, file_size
    :param output_tuples_list: list of tuples
    """
    for parent_path, filename, size in output_tuples_list:
        print("{}\\{}  | size: {} bytes".format(parent_path, filename, size))


def filename(path, root=None):
    """
    Helper method to parse only the filename from the path and resolve any symbolic links if any were found
    :param path: full file path
    :param root: optional parameter of the root path
    :return: filename
    """
    if root is not None:
        path = os.path.join(root, path)

    # Get the tail part of the path (filename or last dir)
    name = os.path.basename(path)

    # For Non Windows Filesystems
    # Verify if directory is valid
    if os.path.islink(path):
        # Resolves any symbolic links
        realpath = os.readlink(path)
        name = '{} -> {}'.format(os.path.basename(path), realpath)

    return name


def get_file_size(full_file_path):
    """
    Get file size in bytes using os.path.getsize for an absolute path of a file
    :param full_file_path path string
    """
    try:
        return os.path.getsize(os.path.join(full_file_path))
    except FileNotFoundError:
        print("The system can not find the file {}".format(full_file_path))
        return -1


def ptree_revised(startpath):
    """
    Main driver to iterate over each directory, subdirectories and files found inside
    :param startpath: input path
    :return: list of typles containing full parent directory path, filename, file size
    """
    result = []

    for root, dirs, files in os.walk(startpath):
        for f in files:
            result.append((root, filename(f, root=root), get_file_size(os.path.join(root, f))))

    return result


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Enter a directory path string to print all its contents and '
                                                 'its subdirectories contents sorted by size')
    parser.add_argument('-p', '--path', dest='path', help="Full absolute path")

    args = parser.parse_args()
    path = args.path

    # Preprocess any backslashes in Windows filesystems
    if os.name =='nt' and '\\' in path:
        path = path.split('\\')
        print(path)
        path = os.path.join(*path)
        print(path)

    r = ptree_revised(path)
    r.sort(key=lambda x: x[2])
    print_list(r)

