import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    paths = os.listdir(path) #the sub directories/files part of this directory

    good_paths = [] #all the files with the file name suffic

    for p in paths: #iterate through the paths

        full_path = path + "/" + p

        if os.path.isfile(full_path):
            if (path + "/" + p).endswith(suffix):
                good_paths.append(path + "/" + p)
        else:
            more_paths = find_files(suffix, full_path)
            for more in more_paths:
                good_paths.append(more)
    return good_paths

print(find_files(".c", "testdir"))
#prints: ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/t1.c']
print(find_files(".h", "testdir"))
#prints: ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h']
print(find_files(".gitkeep", "testdir"))
#prints: ['testdir/subdir2/.gitkeep', 'testdir/subdir4/.gitkeep']
