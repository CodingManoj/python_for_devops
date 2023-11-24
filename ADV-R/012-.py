# Let's talk some modules to execute some commands related to subProcess 

# When you run python script, all the commands that you execure will be a part of the same PID of the script.
# Let's say if you want to execute some of the options / commands with in the script as a sub-process, then you need certain modules.

# google --> python subprocess module ( subprocess management )
# Ref: https://docs.python.org/3/library/subprocess.html

import subprocess 

subprocess.run(["ls", "-l"])


