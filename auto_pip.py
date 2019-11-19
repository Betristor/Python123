import os
libs = ["tensorflow","mxnet"]
for lib in libs:
    os.system("pip install " + lib)