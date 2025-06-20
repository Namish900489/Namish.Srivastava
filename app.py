from flask import Flask, render_template, request

app = Flask(__name__)

def explain_error(error_msg):
    if "SyntaxError" in error_msg:
        return "🧠 SyntaxError usually means there's a typo or incorrect Python syntax."
    elif "NameError" in error_msg:
        return "🔍 NameError means you're using a variable that hasn't been defined."
    elif "IndexError" in error_msg:
        return "📦 IndexError means you're trying to access an index that doesn't exist."
    else:
        return "⚠️ Unknown error - please try to paste the full message."

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    if request.method == "POST":
        error_input = request.form.get("error_text")
        explanation = explain_error(error_input)
    return render_template("index.html", explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
