from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

distilled_student_sentiment_classifier = pipeline(
    'text-classification',
    model='model',
    top_k=None,
)

@app.route('/')
def index():
    return "<p>Listening</p>"

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    data = request.json
    text = data.get('text', '')

    try:
        scores = distilled_student_sentiment_classifier(text).pop()
        
        sentiment = {}
        for score in scores:
            sentiment[score['label']] = score['score']
        
        return jsonify(success=True, sentiment=sentiment)
    except:
        return jsonify(success=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
