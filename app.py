import os
from flask import Flask, request, render_template_string, jsonify
from flask_cors import CORS
import deepseek  # Hypothetical DeepSeek Python package

# Configure DeepSeek API key (if required)
deepseek.api_key = os.environ.get("DEEPSEEK_API_KEY")

app = Flask(__name__)
CORS(app)

# HTML template for the homepage and result display
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DeepSeek as a Judge</title>
</head>
<body>
    <h1>DeepSeek as a Judge</h1>
    <form action="/judge" method="post">
        <textarea name="submission" rows="10" cols="50" placeholder="Enter your submission here..."></textarea><br>
        <button type="submit">Judge Submission</button>
    </form>
    {% if judgment %}
    <h2>Judgment:</h2>
    <p>{{ judgment }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/judge", methods=["POST"])
def judge():
    submission = request.form.get("submission")
    if not submission:
        return jsonify({"error": "No submission provided."}), 400

    # Construct the prompt for DeepSeek
    prompt = (
        f"You are an impartial judge. Evaluate the following submission and provide a fair, concise judgment:\n\n"
        f"{submission}\n\nJudgment:"
    )

    try:
        # Call DeepSeek's hypothetical judge_text function
        judgment = deepseek.judge_text(prompt)
    except Exception as e:
        judgment = f"Error occurred: {str(e)}"

    return render_template_string(HTML_TEMPLATE, judgment=judgment)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
