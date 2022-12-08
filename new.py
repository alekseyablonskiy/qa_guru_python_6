from zipfile import ZipFile


def files_name():
    with ZipFile('/files/Archive.zip') as zip_file:
        info = zip_file.namelist()
        print(info)