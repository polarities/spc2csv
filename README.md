# .spc to .csv converter for EDAX EDS Spectrum
this tiny python code will allow convert from '.spc(EDAX EDS spectrum)' to '.csv' format that easily read by Excel or Origin

# Purposes
this code written by likulogy with full of love to convert spc to csv file for visualize with Origin. csv file is easily edittable, and compatible with most of Text Editors or Graphing Software as like as Excel or Origin.
## Functionality
- spc to csv conversion in python console.
- get list of all spc file that located in specified directory.

# Usage
this simple code allows convert EDS spectra data from spc to csv format with few lines of code in python console.

to use, you need to specify directory that contains multiple or single spc file as a variables. after that, call `get_spcFile` function with directory input.

if you have an single spc file that specified as a variable, you able to call `convert_spc2csv()` fucntion directly.

finally, use `convert_spc2csv()` function to convert from spc file to csv file that can easily visualized with tools.

```python
import spc2csv

directory = './spcfiles'
spc_fileList = spc2csv.get_spcFile(dir)

for i in spc_fileList:
    spc2csv.convert_spc2csv(str(dir) + '/' + str(i))
```

NOTE : output of `get_spcFile()` function only contains name of file and extensions in the list, so you should manipulate result of `get_spcFile()` function to get proper result as like above.

# Dependencies
## Python Version
- Python 3

## Python Library
- HyperSpy 1.3
- numpy
- os
- csv
