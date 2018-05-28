# Python Code Compiler
Hello, this is a python script to compile your python project and get the compilation error.
This was usefull for me to catch my compilation errors before I could find them suring execution.

## Features :
*	Simple Code compiler
*	Uses PyLint package
*	Displays the file name and the error associated


### How to Run :
*	The compile function takes a parameter. It could be path of an individual file or it can be a path of a root folder which has all the source code of your python project.
```
result = python_code_compiler.complile("../source_path")
if result is False:
   raise Exception('Code has errors')
```

## Credits 
*	PyLint Framework	: 	https://pypi.org/project/pylint/
*	Some online blogs and git accounts which I don't remember

Hope you all like it :)