from flask import Flask, render_template_string
import turtle
import io
import base64

app = Flask(__name__)

def draw_tree():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    def branch(length, t):
        if length <= 5:
            return
        t.forward(length)
        t.right(20)
        branch(length - 15, t)
        t.left(40)
        branch(length - 15, t)
        t.right(20)
        t.backward(length)

    branch(100, t)
    turtle_canvas = turtle.getcanvas().postscript(file=io.StringIO())
    turtle.done()
    return turtle_canvas

@app.route("/")
def render_tree():
    turtle_canvas = draw_tree()
    return render_template_string(
        """
        <html>
        <head></head>
        <body>
            <h1>Turtle Graphics</h1>
            <p>Here's the turtle graphics:</p>
            <img src="data:image/png;base64,{{ turtle_canvas }}" alt="Turtle Graphics">
        </body>
        </html>
        """,
        turtle_canvas=base64.b64encode(turtle_canvas.encode()).decode(),
    )

if __name__ == "__main__":
    app.run()
