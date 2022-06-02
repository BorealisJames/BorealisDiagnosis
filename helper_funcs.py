import os

# scandir_out is the output of os.scandir !!
# scandir output gives a list of string with 'DirEntry <file_name>' this func removes Dir entry from the list
def format_scandir_output(scandir_out):
    dir_list = []
    file_list = []
    for entry in scandir_out :
        if entry.is_dir():
            dir_list.append(entry.name)
        if entry.is_file():
            file_list.append(entry.name)

    scandir_out.close()
    return dir_list, file_list

def get_latest_dir(scandir_out):
    dir_list = []
    file_list = []
    for entry in scandir_out :
        if entry.is_dir():
            dir_list.append(entry.name)
        if entry.is_file():
            file_list.append(entry.name)

    scandir_out.close()
    return dir_list, file_list
