class clsOutput(object):
    def __init__(self):
        self.logs = []
    def write(self, logtext):
        self.logs.append(logtext)
    def getalllogs(self):
        return self.logs

def complile(fileorfoldername):
    from pylint import lint
    from pylint.reporters.text import TextReporter
    pylint_output = clsOutput()
    lint.Run(['--errors-only', fileorfoldername], reporter=TextReporter(pylint_output), exit=False)

    file = {}
    cnt = 0
    for l in pylint_output.getalllogs():
        if "*****" in l:
            key = l.replace("*","")
            if key not in file :
                file[l.replace("*","")] = {}
                continue
        # below warnings are suppressed.
        if "Module 'numpy' has no 'floating' member" in l:
            continue
        if "Too many arguments for format string (too-many-format-args)" in l:
            continue

        if l == "" or "\n" in l:
            continue

        file[key][cnt]=l

    filterederror = {}
    for key,val in file.items():
        if len(val)>0:
            filterederror[key] = val

    cnt = 0
    for key, val in filterederror.items():
        cnt = cnt + len(val)

    if cnt>0:
        print(str(cnt)+" Error(s) Found")
        for key, val in filterederror.items():
            print("File :"+key)
            for key1, val1 in val.items():
                print("Error : " + val1)

        print("Build Failed with {0} error(s)".format(cnt))
        return False
    else:
        print("Build Succeeded")
        return True
