# Command Live Arg's vs Environment Variables

$ python calci 10 plus 30    ( 10 is arg1, plus is arg2, 30 is arg3 )

> using the default module sys.argv[1] we can take the values from the command line.

The module we use here is to take command line arguments is `sys` which comes by default and you don't have to install with pip


# Environment Varaibles : We would be using this to read the sensitive information.

ENV Vars vs CMD Live Args : All sensitive info needs to be dealt using ENV vars.

```
To read ENV Variables, we need to import a package called os.

import os 
```

You can see all the environment variables using env on your shell or you can even export any specific variables of your choice using
```
    export token="asdfasdfaerqwedvdsfgvdtq34erdgcv"
```

To read the environment variable inside the script ?

```
    os.getenv("varName")
```
