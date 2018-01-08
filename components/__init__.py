
import os, sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0])


def load_components(obj):
    files = os.listdir(os.path.split(os.path.realpath(__file__))[0])
    files.remove("__init__.py")
    files.remove('__pycache__')
    #files.append('assadfsdfsdf123.py')
    for filename in files:
        filesplit = os.path.splitext(filename)
        if filesplit[1] == '.py':
            __import__(filesplit[0]).load(obj)
            '''
            try:
                __import__(filesplit[0]).load(obj)
            except BaseException:
                print("Error: (Components) - '%s' Load failure" % filesplit[0])
                exit()
            '''
