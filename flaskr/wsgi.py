import multiprocessing

import gunicorn.app.base
import __init__

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8080'),
        'workers': number_of_workers(),
    }
    __init__.create_app(handler_app, options).run()


