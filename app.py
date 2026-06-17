from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    expression = ""
    if request.method == 'POST':
        expression = request.form.get('expression')
        value = request.form.get('value')
        if value == "C":
            expression = ""
        elif value == "=":
            try : 
                expression = str(eval(expression))
            except:
                expression = "Invalid Input"
        else:
            expression += value
    return render_template('index.html' , expression = expression)


if __name__ == "__main__":
    app.run(debug=True)
