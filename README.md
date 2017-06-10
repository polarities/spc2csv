# .spc to .csv converter for EDAX EDS Spectrum
this tiny python code will allow convert from '.spc(EDAX EDS spectrum)' to '.csv' format that easily read by Excel or Origin

# Purposes
this code written by likulogy with full of love to convert spc to csv file for visualize with Origin. csv file is easily edittable, and compatible with most of Text Editors or Graphing Software as like as Excel or Origin.

# Usage
this simple code allows convert EDS spectra data from spc to csv format with few lines of code in python console.

to use, you need to specify directory that contains multiple or single spc file as a variables. after that, call get_spcFile function with directory input.

and, use convert_spc2csv() function to convert from spc file to csv file that can easily visualized with tools.

```python
directory = './spcfiles'
spcl = spc2csv.get_spcFile(dir)

for i in spcl:
    spc2csv.convert_spc2csv(str(dir) + '/' + str(i))
```

# Dependencies


