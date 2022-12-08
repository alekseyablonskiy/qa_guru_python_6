import os
from zipfile import ZipFile
import csv
from PyPDF2 import PdfReader
from openpyxl import load_workbook


# file size comparison
def test_archive_size():
    assert os.path.getsize('../files/Archive.zip') == 80496


# archive files name comparison
def test_file_names():
    with ZipFile('../files/Archive.zip') as zip_file:
        info = zip_file.namelist()
        assert info == ['csv_file.csv', 'pdf_file.pdf', 'xlsx_file.xlsx']


# unzipping files
def test_count_files():
    with ZipFile('../files/Archive.zip') as zip_file:
        zip_file.extractall('../files')
        assert len(os.listdir('../files')) == 4


# read csv file
def test_read_csv():
    with open('../files/csv_file.csv') as csvfile:
        csv_rows = csv.reader(csvfile)
        new_list = []
        for row in csv_rows:
            new_list.append(row)
        assert len(new_list) == 5
        assert new_list == [['1', 'Python', '31%'],
                            ['2', 'Java', '17%'],
                            ['3', 'JavaScript', '8%'],
                            ['4', 'C#', '7%'],
                            ['5', 'PHP', '6%']]


# read pdf file
def test_read_pdf():
    reader = PdfReader('../files/pdf_file.pdf')
    assert len(reader.pages) == 1
    page = reader.pages[0]
    text = page.extract_text()
    assert 'Hello, world!' in text


# read xlsx file
def test_read_xlsx():
    workbook = load_workbook('../files/xlsx_file.xlsx')
    sheet = workbook.active
    assert sheet.cell(row=1, column=2).value == 'Aleksey'


# delete files
def test_file_deleted():
    os.remove('../files/csv_file.csv')
    os.remove('../files/pdf_file.pdf')
    os.remove('../files/xlsx_file.xlsx')
    assert len(os.listdir('../files')) == 1