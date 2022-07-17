import glob
import os
import time
import shutil

# Path to the file/directory
path_inp = "D:\\Camera\\*.*"
path_out = "D:\\Sorted\\"

i = 1
for file in glob.glob(path_inp):
    ti_m = os.path.getmtime(file)
    md_time = time.ctime(ti_m)
    t_obj = time.strptime(md_time)
    year_month_stamp = time.strftime("%Y-%m", t_obj)
    date_stamp = time.strftime("%Y-%m-%d", t_obj)
    path = path_out + year_month_stamp + "\\" + date_stamp

    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)

    # new_path = shutil.move(file, path)
    new_path = shutil.copy(file, path)
    print(i, new_path)
    i += 1
