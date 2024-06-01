from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b. - /add?a=_&b=_"""
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Subtract b from a."""
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    """Divide a by b."""
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)