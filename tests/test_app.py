from app import index
from flask import Flask, render_templat



def test_index():
    #assert index() == "surendra python dev"
    assert index() == render_template('python.html') 
