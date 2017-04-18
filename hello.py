#!/usr/bin/env python
import sys 
import subprocess

print ('Hello world')
print ('Another hello to tests git pull command')

subprocess.check_output(["echo", "Hello World!"])
subprocess.check_call(["ls", "-l"])
