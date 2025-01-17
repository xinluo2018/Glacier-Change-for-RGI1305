#! /bin/bash 
## author: xin luo;
## create: 2022.05.15;
## des: 1) readout the download icesat1 glas14 data by tile, and
##      2) subset and write out.
## usage: icesat_readout.sh -y 2003

cd /home/xin/Developer-luo/Glacier-in-SETP

bottom=27; up=32; left=91; right=99;
year=2022  ## default

# Get the options
while getopts "y:" arg; do
   case $arg in
      y) # Enter a year
         year=$OPTARG;;
      ?) # Invalid argment
         echo "Error: Invalid argment"
         exit;;
   esac
done


### -- 1. readout icesat GLAH14/ATL06 data (selected variables).
### setting
if [[ "2003 2004 2005 2006 2007 2008 2009" == *"$year"* ]]; then      
  dir_data=data/icesat-1/GLAH14-$year
  func_read=utils/read_glah14.py
else
  dir_data=data/icesat-2/ATL06-$year
  func_read=utils/read_atl06.py
fi

paths_file_raw=$(ls $dir_data/raw/*)
echo $paths_file_raw
dir_readout=$dir_data/readout
if [ ! -d $dir_readout ]; then mkdir $dir_readout 
fi

### 1.readout the icesat data
python $func_read $paths_file_raw -o $dir_readout -n 4 

### -- 2. subset to the specific region
python utils/subset_file.py $dir_readout/*_readout.h5 -r $left $right $bottom $up      

### -- 3. delete medium files
rm $dir_readout/*_readout.h5

