# importing from nose module
from nose.tools import * # importing all members
import project

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("RAN SUCCESSFULLY!")
