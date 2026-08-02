import os, glob

files = glob.glob('testing/*.py') + glob.glob('privet/onyx_reports/*.py')
files_with_time = [(f, os.path.getmtime(f)) for f in set(files)]
files_with_time.sort(key=lambda x: x[1])

for f, t in files_with_time:
    import datetime
    dt = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    print(f"{dt}  {f}")
