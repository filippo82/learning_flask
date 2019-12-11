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

### Tips

* The name of the route and the name of the view function do **not** have to match.
