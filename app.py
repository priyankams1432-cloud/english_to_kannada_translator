"""
English to Kannada Translator with Text-to-Speech
A Flask web application that translates English text to Kannada and generates speech.
"""

from flask import Flask, render_template, request, jsonify
import os
import requests
from gtts import gTTS

app = Flask(__name__, static_folder='static', template_folder='templates')


# Translation mapping (common phrases)
TRANSLATION_MAP = {
    'hello': 'ನಮಸ್ಕಾರ',
    'good morning': 'ಶುಭೋದಯ',
    'good night': 'ಶುಭರಾತ್ರಿ',
    'thank you': 'ಧನ್ಯವಾದ',
    'how are you': 'ನೀವು ಹೇಗಿದ್ದೀರಿ',
    'my name is': 'ನನ್ನ ಹೆಸರು',
    'welcome': 'ಸ್ವಾಗತ',
    'sorry': 'ಕ್ಷಮಿಸಿ',
    'yes': 'ಹೌದು',
    'no': 'ಅಲ್ಲ',
    'water': 'ನೀರು',
    'food': 'ಆಹಾರ',
    'friend': 'ಸ್ನೇಹಿತ',
    'family': 'ಕುಟುಂಬ',
    'love': 'ಪ್ರೀತಿ',
}


def translate_to_kannada(text):
    """Translate English text to Kannada using simple mapping."""
    text_lower = text.lower().strip()
    
    # Check for direct matches
    if text_lower in TRANSLATION_MAP:
        return TRANSLATION_MAP[text_lower]
    
    # Check for partial matches in the text
    for english, kannada in TRANSLATION_MAP.items():
        if english in text_lower:
            return kannada
    
    # Fallback: Use online translation API
    try:
        # Using MyMemory Translation API (free, no auth needed)
        response = requests.get(
            'https://api.mymemory.translated.net/get',
            params={'q': text, 'langpair': 'en|kn'},
            timeout=5
        )
        if response.status_code == 200:
            result = response.json()
            return result['responseData']['translatedText']
    except:
        pass
    
    # Final fallback
    return f"[ಕನ್ನಡ ಅನುವಾದ: {text}]"


@app.route('/')
def index():
    """Render the main translator page."""
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    """Translate English text to Kannada and generate audio."""
    data = request.get_json() or {}
    text = (data.get('text') or '').strip()
    
    if not text:
        return jsonify({'error': 'Please enter some text to translate'}), 400
    
    if len(text) > 5000:
        return jsonify({'error': 'Text is too long (max 5000 characters)'}), 400

    try:
        # Translate text to Kannada
        kannada_text = translate_to_kannada(text)
        
        # Generate speech
        output_dir = os.path.join(os.path.dirname(__file__), 'static', 'audio')
        os.makedirs(output_dir, exist_ok=True)
        
        audio_path = os.path.join(output_dir, 'output.mp3')
        tts = gTTS(text=kannada_text, lang='kn', slow=False)
        tts.save(audio_path)
        
        return jsonify({
            'success': True,
            'original': text,
            'translated': kannada_text,
            'audio_url': '/static/audio/output.mp3'
        })
    
    except Exception as e:
        return jsonify({'error': f'Translation error: {str(e)}'}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
