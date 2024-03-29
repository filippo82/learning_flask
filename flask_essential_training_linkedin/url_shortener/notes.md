# Flask essential training
This is a LinkedIn Learning course taught by Nick Walter.

### Serve the application

If the main application is inside the `hello.py` file, we serve it by first setting the `FLASK_APP` environment variable and then entering `flask run`:
```shell
export FLASK_APP=hello
flask run
```
However, if the file that contains the main application is called `app.py`, one can just serve it by entering
```shell
flask run
```
because `flask` looks for a default `app.py` file.

### Development environment

```shell
export FLASK_APP=hello
export FLASK_ENV=development
flask run
```

## Templates
Before we can use templates in `flask`, we need to import `render_template`:
```shell
from flask import render_template
```
By default, `flask` looks for templates inside the `templates` directory but this behavior can be changed XXX.

## Data movement

### Parameters
We can pass parameters to the template engine by including them when calling `render_template`:
```shell
return render_template('home.html', name='Filippo')
```
Then, in the template file ()`home.html` in this case), we can use the value of parameter by enclosing it in double curl brackets:
```shell
<h2>{{name}}</h2>
```

### Requests

By default, `flask` treats all requests as `GET` requests.

First, we need to import the `request` submodule:
```shell
from flask import request
```

```shell
@app.route('/your-url', methods=['GET'])
def your_url():
    return render_template('your_url.html', code=request.args['code'])
```

`http://localhost:5000/your-url?code=hello`

```shell
@app.route('/your-url', methods=['POST'])
def your_url():
    return render_template('your_url.html', code=request.form['code'])
```

## HTML

### Forms

#### \<input\>
The `name` attribute of an `<input>` field is used to reference elements in a JavaScript, or to reference form data after a form is submitted.

## Tips

* The name of the route and the name of the view function do **not** have to match.
