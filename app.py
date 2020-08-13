from flask import Flask, render_template
app= Flask(__name__)




@app.route("/")

def hello():
	return render_template("index.html")

@app.route("/spanish.html")
def spanish():
	return render_template("spanish.html")


@app.route("/index.html")
def english():
	return render_template("index.html")
	



if __name__ == "__main__":
    app.run(debug=True)
	