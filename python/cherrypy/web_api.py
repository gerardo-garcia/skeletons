from bottle import Bottle, request
import time

httpserver = Bottle()

@httpserver.get('/stuff')
def do_stuff():
    '''
    Method that does stuff.
    '''
    stuff = {'data': 'some data'}
    time.sleep(5)
    # Return the environment info as Json data
    return stuff

