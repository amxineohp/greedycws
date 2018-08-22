import os
import sys

golden_file = sys.argv[1]
if len(sys.argv)>2:
    s = int(sys.argv[2])
    e = int(sys.argv[3])

def run_cmd(cmd):
    os.system(cmd)
    cmd = 'grep \'F MEASURE\' tmp '
    os.system(cmd)
    cmd = 'rm tmp'
    os.system(cmd)
if len(sys.argv)>2:
    cmd_template = './score ../data/dic %s ../result/dev_result%s > tmp'
    for i in range(s,e+1):
        cmd = cmd_template%(golden_file,i)
        run_cmd(cmd)
else:
    cmd_template = './score ../data/dic %s result > tmp'
    cmd = cmd_template%(golden_file)
    run_cmd(cmd)


