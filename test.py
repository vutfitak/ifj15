#!/usr/bin/env python
"""
 IFJ 15 Test Suite
 Author: Pavol Plaskon <xplask00@stud.fit.vutbr.cz>

 This program is free software: you can redistribute it and/or modify it under
 the terms of the GNU General Public License as published by the Free Software
 Foundation, either version 3 of the License, or (at your option) any later
 version.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 details.
"""

import os
import random
import subprocess
import sys

dash_line = "-------------------------------------"

def print_head(text):
    print(dash_line)
    print(dash_line)
    print("\n{}\n".format(text))
    print(dash_line)


def print_test_head(n, source):
    global to_print
    to_print += dash_line + "\n"
    to_print += "TEST {}: {}\n".format(n, source)


def check_ret_code(returned, expected):
    global to_print
    if returned == int(expected):
        to_print += "Return value: OK\n"
        return True
    else:
        to_print += "Expected return code: {}\nProgram returned: {}\n".format(expected, returned)
        return False


def check_stdout(out, expected):
    global to_print
    if out != expected:
        to_print += "UNexpected output: {}\n".format(out)
        to_print += "Expected: {}\n".format(expected)
        return False
    return True


def check_stderr(err):
    """Expect 'IFJ15' in error output."""
    global to_print
    if 'IFJ15' not in err:
        to_print += "UNexpected error output: {}\n".format(err)
        return False
    return True


def print_statistics(n, n_ok, n_fail, fails):
    print(dash_line)
    print("Number of tests: {}\nSucceed tests: {}\nFAILED: {}\n"
          .format(n, n_ok, n_fail))

    if n_fail != 0:
        print("Failed tests:")
        for k, v in sorted(fails.items()):
            print("TEST {}: {}".format(k,v))


if not(os.path.isfile('ifj') and os.access('ifj', os.X_OK)):
    print("No executable file named 'ifj' found, try 'make'.")
    sys.exit()


#
# OK
#

tests_dir = os.path.join(os.getcwd(), 'tests/tests_ok')

x = 0
x_ok = 0
x_fail = 0
fails = {}
to_print = ''

print_head("IFJ15: Tests without errors.")

for source in [f for f in os.listdir(tests_dir)
              if not f.endswith('.out') and f.startswith('test')]:

    to_print = ''
    x = x + 1
    source_path = os.path.join(tests_dir, source)
    proc = subprocess.Popen(
        ["./ifj", source_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    with open(source_path + '.out', 'r') as f_out:
        expected_out = f_out.read()

    out, err = proc.communicate()
    ret_code = proc.returncode

    print_test_head(x, source)
    c_ret = check_ret_code(ret_code, 0)
    c_out = check_stdout(out, expected_out)
    c_err = not err

    if c_ret and c_out and c_err:
        x_ok = x_ok + 1
    else:
        print(to_print)
        x_fail = x_fail + 1
        fails[x] = source


#
# Error tests
#

tests_dir = os.path.join(os.getcwd(), 'tests')

fx = 0
fx_ok = 0
fx_fail = 0
ffails = {}


print_head("IFJ15: Tests containing some errors.")

for source in [f for f in os.listdir(tests_dir)
              if os.path.isfile(os.path.join(tests_dir, f)) and
              f.startswith('test')]:

    to_print = ''
    fx = fx + 1
    source_path = os.path.join(tests_dir, source)
    proc = subprocess.Popen(['./ifj', source_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True
    )

    out, err = proc.communicate()
    ret_code = proc.returncode

    print_test_head(fx, source)
    exp_ret = source[-2:] if source[-2].isdigit() else source[-1]
    c_ret = check_ret_code(ret_code, exp_ret)
    c_out = check_stdout(out, '')
    # c_err = check_stderr(err.decode('utf-8'))
    if c_ret and c_out:  # and c_err: dont't care about stderr
        fx_ok = fx_ok + 1
    else:
        print(to_print)
        fx_fail = fx_fail + 1
        ffails[fx] = source

print_head('RESULTS')
print("Tests for correct source files:")
print_statistics(x, x_ok, x_fail, fails)
print(dash_line)
print("Tests for incorrect source files:")
print_statistics(fx, fx_ok, fx_fail, ffails)
