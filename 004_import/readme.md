# What's next ?

```
Functions Modules & Packages
```

### Virtual Environment : It is also referred as Python Worksaces

### Function : what and why ?

*Module :* This is like source in bash, you delcared lot of functions in a abc.py file and you can use it another project or anywhere, by importing that module. This can also be called as source in bash scripting. The advantage is resuability. A module is nothing but a group of functions. We 

*Function :* This is also referred as a definition.

```
Functions should always take input and execute the task and return the output.
```

> To Be Notes : 
```
1) Avoid using - in the fileNames of python scripts, this is due to the fact when you import that file as a module in another python script using import, impost don't allow - or 001 or start of the files as numbers.

```

### Function : A set of task or tasks defined in a file

### Module : Collection Of Functions In a file

### Package or Library : Collection of modules : As a DevOps Engineers, we consume packages that are written by devs, we mostly create our own Modules & Functions. We are more at the consumer end. If you've your code written in multiple files, you can bundle them in to a package


What is PYPI : Python Package Index : Usually if any of the product needs to be exposed to the public, dev's write the code and will publish the libraries to Python Artifactory or PYPI ( In Python world we call it as PYPI ). Where anyone in the internet can use this MODULE published using import in their code.

PYPI is just like docker hub : google ---> PYPI and search for the packages of your choice.

> Using pip or pip3, we can install any of the packages available in the PYPI.
    Ex : pip install boto , pip install jira ...

### Virtual Environment :

```
In general we use common machines for all sort of works, 
    Project 1 wants to use confluence for 1.2.3
    Project 2 wants to use confluence for 1.2.5

How can we solve and satisfy all of them with a single machine. That's where, Virtual Environment does.

It's going to provison a logical environment on your machine.

Using this concept, we can create multiple environments on the same machine woth multiple python package verisons. 
To use virtual env on your linux box, you need to install

$   pip3 install virtualenv

```

### How to create Virtual Env for project-a,b,c ?

```
$ python -m venv projetct-a           # This creates a folder called as project-a
$ python -m venv projetct-b           # This creates a folder called as project-b
$ python -m venv projetct-c           # This creates a folder called as project-c

```