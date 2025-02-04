import shutil
import os


def copy_all(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    list_dir = os.listdir(source)
    for item in list_dir:

        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if ( os.path.isfile(source_path)):
            print(f"Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)

        else:
            print(f"Copying directory: {source_path} -> {dest_path}")
            copy_all(source_path, dest_path)