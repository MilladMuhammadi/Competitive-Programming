#!/usr/bin/env python3
import random
import os
import shlex
import shutil
import subprocess
import sys

MAX_N = 2 * 10**5
MAX_H = 10**9
random.seed(2020)



MAKE_DATA = len(sys.argv) >= 2 and sys.argv[1] == 'makedata'
CASE = 1
manual_cases = set()
def add_case(name, cmd):
    print('      - %s: %s' % (name, cmd))
    if os.path.isfile(cmd) and os.path.splitext(cmd)[1] == '.in':
        manual_cases.add(cmd)
    if MAKE_DATA:
        global CASE
        dst = os.path.join('..', 'data', 'secret', '%02d-%s.in' % (CASE, name))
        CASE += 1
        if cmd in manual_cases:
            shutil.copyfile(cmd, dst)
            sys.stderr.write('Copying %s to %s\n' % (cmd, dst))
        else:
            cmd = shlex.split(cmd)
            cmd[0] = './' + cmd[0]
            sys.stderr.write('Running %s > %s\n' % (cmd, dst))
            with open(dst, 'w') as f:
                subprocess.run(cmd, stdout=f, check=True)



print('''## AUTO-GENERATED BY gen-yaml.py, DO NOT EDIT
solution: /submissions/accepted/per_nlogn.cc

data:
  sample:
    type: directory
    solution:
    data:
      '1':
      '2':
      '3':
      '4':

  secret:
    type: directory
    data:''')
                
add_case('small_manual_across', 'manual/across.in')
add_case('small_manual_split', 'manual/split.in')
add_case('small_manual',  'manual/small.in')
add_case('small_manual' , 'manual/misc1.in')
add_case('small_manual' , 'manual/misc2.in')
add_case('single_stack', 'uniform.py --maxn 1')
add_case('single_stack_empty', 'uniform.py --maxn 1 --maxh 0')
for i in range(5):
    add_case('small_uniform_low' , 'uniform.py --maxn 10 --maxh 10 --seed %d' % i)
for i in range(3):
    add_case('big_uniform_low' ,'uniform.py --maxh 10 --seed %d' % (i + 10))
add_case('big_uniform_medium', 'uniform.py --maxh %d --seed 15' % (MAX_N//4))
add_case('big_uniform_high' , 'uniform.py --seed 16')
for i in range(2):
    add_case('big_few_peaks', 'fewpeaks.py %d %d %d %d %d --seed %d' %
             (MAX_N//2, MAX_N-MAX_N//2-10, 9, 1, 0, i+20))
for i in range(2):
    add_case('big_few_peaks', 'fewpeaks.py %d %d %d %d %d --seed %d' %
             (MAX_N//2, MAX_N-MAX_N//2-2, 0, 0, 2, i+30))
for i in range(2):
    add_case('big_few_peaks', 'fewpeaks.py %d %d %d %d %d --seed %d' %
             (95*MAX_N//100, MAX_N-95*MAX_N//100-3, 0, 3, 0, i+40))
add_case('max_all_zeros', 'uniform.py --minn %d --maxh 0' % MAX_N)
add_case('max_all_ones', 'uniform.py --minn %d --minh 1 --maxh 1' % MAX_N)
add_case('max_uniform_balanced', 'uniform.py --minn %d --maxh 2' % MAX_N)
add_case('max_answer', 'uniform.py --minn %d --minh %d' % (MAX_N, MAX_H))
add_case('anti_quadratic', 'antiquadratic1.py %d %d 1' % (MAX_N, MAX_N//2))
add_case('anti_quadratic', 'antiquadratic1.py %d %d 2' % (MAX_N, MAX_N//2))
add_case('anti_quadratic', 'antiquadratic2.py %d %d -1' % (MAX_N, MAX_N//2))
add_case('anti_quadratic', 'antiquadratic2.py %d %d -1' % (MAX_N, 2*MAX_N//3))
add_case('anti_quadratic', 'antiquadratic2.py %d %d 1' % (MAX_N, MAX_N//2))
add_case('anti_quadratic', 'antiquadratic2.py %d %d 1' % (MAX_N, MAX_N//3))
add_case('big_dense', 'manual/big.in')
add_case('big_sparse', 'manual/big_sparse1.in')
add_case('bug_ragnar', 'fewpeaks.py 4 4 0 0 0 --seed 1497354887')
add_case('big_geometric_balanced', 'geometric.py --n %d --seed 51' % MAX_N)
add_case('big_geometric_fewerblocks', 'geometric.py --n %d --p 0.6 --seed 52' % MAX_N)
add_case('big_geometric_moreblocks', 'geometric.py --n %d --p 0.4 --seed 53' % MAX_N)
for i in range(4):
    blocks = MAX_N + int(random.normalvariate(0, 100))
    add_case('big_%d_blocks_into_%d_stacks' % (blocks, MAX_N), 'ballsintobins.py --n %d --blocks %d --seed %d' %
             (MAX_N, blocks, 100+i))

print('#     Before editing this file, read comment on first line of file.')

for (p, _, files) in os.walk('manual'):
    for f in files:
        path = os.path.join(p, f)
        if path not in manual_cases:
            sys.stderr.write('Manual case %s not added, did you forget it?\n' % path)
