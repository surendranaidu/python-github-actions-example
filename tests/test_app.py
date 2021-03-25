from app import index
#from flask import Flask, render_templat



def test_index():
    a,b =index()
    assert b == "surendra python dev"
    #assert index() == render_template('python.html') 
