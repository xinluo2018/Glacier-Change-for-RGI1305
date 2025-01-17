# author: xin luo 
# creat: xin luo, 2023.1.17.   
# des: download the crytempo eolis point data.
# usage: 1) search the data from the cs2eo.org(https://cs2eo.org/cryotempo) website. 2) replace the esa_files (below) with the download script from the cs2eo.org website.

import os
import platform
from ftplib import FTP
import sys
import shutil

email = 'xinluo_xin@163.com'   # should be replaced by the user's email.
dir_down = '/home/xin/Developer-luo/Glacier-in-SETP/data/cryosat-2/tempopoint-2021/raw-2/'
### should be replaced by the search cryosat files from cs2eo.org(https://cs2eo.org/cryotempo)
esa_files = ['/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+96458358_+29220461_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+92388573_+30446348_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+91140476_+27834394_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+96458358_+29220461_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+93350800_+29487168_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+96458358_+29220461_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+90119057_+27885152_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+95424706_+29318642_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+97360615_+28226165_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+93439321_+30375429_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+95534915_+30205429_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+93264113_+28597180_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+94589696_+31181092_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+92310987_+29557468_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+94488178_+30295115_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+96339900_+28332701_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+97489521_+29113035_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+90226760_+29670049_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+97360615_+28226165_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+92310987_+29557468_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+92235012_+28666888_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+92235012_+28666888_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+94488178_+30295115_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+93264113_+28597180_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+93439321_+30375429_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+92160596_+27774437_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+98953635_+31643339_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+92388573_+30446348_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+98953635_+31643339_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+93350800_+29487168_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+92160596_+27774437_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+90119057_+27885152_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_11_+94589696_+31181092_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+97489521_+29113035_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/11/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_11_+95424706_+29318642_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+90172348_+28778515_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/SOUASIAEA/CS_OFFL_THEM_POINT_SOUASIAEA_2021_10_+96339900_+28332701_V102.nc', '/TEMPO_SWATH_Baseline-1/TEMPO_SWATH_POINT/2021/10/CENTRASIA/CS_OFFL_THEM_POINT_CENTRASIA_2021_10_+94388780_+29407552_V102.nc']

download_file_obj = None
read_byte_count = None
total_byte_count = None

def get_padded_count(count, max_count):
    return  str(count).zfill(len(str(max_count)))

def file_byte_handler(data):
    global download_file_obj, read_byte_count, total_byte_count
    download_file_obj.write(data)
    read_byte_count = read_byte_count + len(data)
    progress_bar(read_byte_count, total_byte_count)


def progress_bar(progress, total, prefix="", size=60, file=sys.stdout):
    if total != 0:
        x = int(size*progress/total)
        x_percent = int(100*progress/total)
        file.write(f" {prefix} [{'='*x}{' '*(size-x)}] {x_percent} % \r")
        file.flush()


def download_files(user_email):
    global download_file_obj, read_byte_count, total_byte_count, esa_files
    print("About to connect to ESA science server")
    with FTP("science-pds.cryosat.esa.int") as ftp:
        try:
            ftp.login("anonymous", user_email)
            print("Downloading {} files".format(len(esa_files)))
            
            for i, filename in enumerate(esa_files):
                padded_count = get_padded_count(i+1, len(esa_files))
                print("{}/{}. Downloading file {}".format(padded_count, len(esa_files), os.path.basename(filename)))
                
                with open(os.path.basename(filename), 'wb') as download_file:
                    download_file_obj = download_file
                    total_byte_count = ftp.size(filename)
                    read_byte_count = 0
                    ftp.retrbinary('RETR ' + filename, file_byte_handler, 1024)
                    shutil.move(os.path.basename(filename), dir_down+os.path.basename(filename))
                print("\n")
        finally:
            print("Exiting FTP.")
            ftp.quit()


if __name__ == '__main__':
    if int(platform.python_version_tuple()[0]) < 3:
        exit("Your Python version is {}. Please use version 3.0 or higher.".format(platform.python_version()))
    # email = input("Please enter your e-mail: ")    
    download_files(email)
    
