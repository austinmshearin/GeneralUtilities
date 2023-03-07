"""
Package for handling basic file transfer processes
"""
# Standard Imports
import time
import os
import shutil

def get_all_files(folderpath: str, file_extension: str = None) -> tuple:
    """
    Gets all files within the specified folder and sub-folders with a specified file extension

    Parameters
    ----------
    folderpath: str
        Filepath to folder with all data
    file_extension: str (optional)
        Filter files returned to having a specified file extension

    Returns
    -------
    tuple
        list of all files, list of all relative paths, list of all full filepaths
    """
    filepaths = []
    for dirpath, _, filenames in os.walk(folderpath):
        for file in filenames:
            if file_extension is None:
                filepaths.append(os.path.join(dirpath, file))
            else:
                len_extension = len(file_extension)
                if file[-len_extension:] == file_extension:
                    filepaths.append(os.path.join(dirpath, file))
    relpaths = [filepath.replace(folderpath, '')[1:] for filepath in filepaths]
    files = [os.path.basename(filepath) for filepath in filepaths]
    return (files, relpaths, filepaths)

def get_file_extension(filepath: str) -> str:
    """
    Gets the file extension of the filepath

    Parameters
    ----------
    filepath: str
        Filepath for the file to get the file extension of

    Returns
    str
        File extension of the file
    """
    return filepath[max([index for index, char in enumerate(filepath) if char == "."]):]

def transfer_files(source: str, destination: str, file_extension: str = None, progress_output: bool = True,
    destination_suffix: str = None, copy: bool = True):
    """
    Transfer files and mimic folder structure from source to destination

    Parameters
    ----------
    source: str
        Filepath of source data
    destination: str
        Filepath for destination of data
    file_extension: str = None
        Include only files with specific file extension
    progress_output: bool = True
        Function will output details of process to terminal
    destination_suffix: str = None
        Adds a suffix to the filename to all files copied to the destination folder
    copy: bool = True
        If True, files will be copied from source to destination
        If False, files will be deleted from source after transfer
    """
    # Check file_extension for period
    if file_extension is not None:
        if file_extension[0] != ".":
            file_extension = "." + file_extension
    # Check all files at source
    _, source_relpaths, _ = get_all_files(source, file_extension)
    # Check all files at destination
    _, destination_relpaths, _ = get_all_files(destination, file_extension)
    if destination_suffix is not None:
        if file_extension is not None:
            destination_relpaths = [relpath.replace(destination_suffix+file_extension, file_extension) \
                for relpath in destination_relpaths]
        else:
            destination_relpaths = [
                relpath.replace(
                    destination_suffix + get_file_extension(relpath), 
                    get_file_extension(relpath)
                    )
                for relpath in destination_relpaths
                ]
    # Determine files that need to be transferred
    files_to_duplicate = list(set(source_relpaths).difference(destination_relpaths))
    # Transfer missing files from source to destination
    if progress_output:
        num_files = len(files_to_duplicate)
        counter = 0
        print("Copying {0} files".format(str(num_files)))
    time.sleep(3)
    for file in files_to_duplicate:
        filepath = os.path.join(source, file)
        new_filepath = os.path.join(destination, file)
        if destination_suffix is not None:
            if file_extension is not None:
                new_filepath = new_filepath.replace(file_extension, destination_suffix+file_extension)
            else:
                temp_file_extension = get_file_extension(new_filepath)
                new_filepath = new_filepath.replace(temp_file_extension, destination_suffix+temp_file_extension)
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
        shutil.copyfile(filepath, new_filepath)
        if copy is False:
            os.remove(filepath)
        if progress_output:
            counter += 1
            if (counter % 1000 == 0) or (counter == num_files):
                print("Transferred {0}/{1} files".format(str(counter),str(num_files)))

def delete_all_files(directory: str, progress_output: bool = True):
    """
    Deletes all files within the specified directory and subdirectories

    Parameters
    ----------
    directory: str
        Filepath to the directory to delete
    progress_output: bool = True
        Function will output details of process to terminal

    Notes
    -----
    Retains the directory structure
    """
    _, _, filepaths = get_all_files(directory)
    if progress_output:
        num_files = len(filepaths)
        counter = 0
    for file in filepaths:
        os.remove(file)
        if progress_output:
            counter += 1
            if (counter % 1000 == 0) or (counter == num_files):
                print("Deleted {0}/{1}".format(str(counter),str(num_files)))

def zip_directory(directory: str, output_file: str):
    """
    Zip the directory into a zip file

    Parameters
    ----------
    directory: str
        Filepath of the directory to zip
    output_file: str
        Filepath for the zipped directory file
    """
    shutil.make_archive(output_file, 'zip', directory)
