from flask import Flask, render_template , url_for, send_from_directory
app = Flask(__name__)

posts = [
    {
        "writer": "isaac",
        "headline": "Starting out with flask",
        "post_body": "this is the content we signed up for",
        "date": "July 30, 2022"
    },
        {
        "writer": "eve",
        "headline": "Loving this",
        "post_body": "this is the content we signed up for",
        "date": "   Jan 40, 2004"
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about us.html', title="About Us")

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(debug=True)