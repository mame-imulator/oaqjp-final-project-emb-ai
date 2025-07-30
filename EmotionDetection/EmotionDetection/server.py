from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():

    text = request.form.get('text') or request.json.get('text')
    
    if not text:
        return "Error: No text provided.", 400
    
    try:
        result = emotion_detector(text)

        anger = result['anger']
        disgust = result['disgust']
        fear = result['fear']
        joy = result['joy']
        sadness = result['sadness']
        dominant = result['dominant_emotion']

        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant}."
        )

        return formatted_response

    except Exception as e:
        return f"Error during emotion detection: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
