from flask import Flask

app = Flask( __name__ )


@app.route('/hello')
@app.route( '/hello/<name>' )
def hello_world(name='aaaa'):
    return 'Hello World! %s' % name


if __name__ == '__main__':
    app.run()
