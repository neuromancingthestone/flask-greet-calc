from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO WORLD"

@app.route('/add')
def add():
    print(request.form)
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"""
        <b>{operations.add(a,b)}</b>
    """
    return html

@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"""
        <b>{operations.sub(a,b)}</b>
    """
    return html

@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"""
        <b>{operations.mult(a,b)}</b>
    """
    return html

@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"""
        <b>{operations.div(a,b)}</b>
    """
    return html

@app.route('/<operation>')
def ops(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])    
    if operation == "add":
        html = f"""
            <b>{operations.add(a,b)}</b>
        """   
    elif operation == "sub":
        html = f"""
            <b>{operations.sub(a,b)}</b>
        """      
    elif operation == "mult":
        html = f"""
            <b>{operations.mult(a,b)}</b>
        """  
    elif operation == "div":
        html = f"""
            <b>{operations.div(a,b)}</b>
        """                        
    else:
        html = """
            Invalid Operation Call
        """
    return html   