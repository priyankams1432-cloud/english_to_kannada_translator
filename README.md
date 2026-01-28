# 🌐 English to Kannada Translator

A modern, user-friendly web application that translates English text to Kannada and generates text-to-speech audio using Flask, HTML, and CSS.

## ✨ Features

- **Real-time Translation**: Translate English text to Kannada instantly
- **Text-to-Speech**: Generate natural-sounding Kannada audio
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Beautiful UI**: Modern gradient design with smooth animations
- **Character Counter**: Real-time character count with 5000 character limit
- **Copy Function**: Easily copy translated text to clipboard
- **Error Handling**: Comprehensive error messages for better user experience
- **Fast Performance**: Optimized backend for quick translations

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Translation API**: Google Translate (via googletrans)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Styling**: Custom CSS with CSS Grid and Flexbox

## 📋 Requirements

- Python 3.7+
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Installation

### 1. Clone/Download the Project

```bash
cd english_to_kannada_translator
```

### 2. Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

All required packages will be installed:
- Flask (web framework)
- googletrans (translation API)
- gTTS (text-to-speech)
- requests (HTTP library)

## 🎯 Usage

### Starting the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Using the Translator

1. **Enter Text**: Type or paste English text in the textarea
2. **Translate**: Click the "Translate & Play" button
3. **View Results**: 
   - See original English text
   - View Kannada translation
   - Listen to audio pronunciation
4. **Copy**: Use the "Copy Translation" button to copy text to clipboard

### Keyboard Shortcuts

- **Ctrl + Enter**: Translate the text quickly

## 📁 Project Structure

```
english_to_kannada_translator/
├── app.py                 # Flask application (backend)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── static/
│   ├── style.css         # CSS styling
│   └── audio/            # Generated audio files (auto-created)
└── templates/
    └── index.html        # HTML template (frontend)
```

## 🔧 Configuration

### Changing the Port

Edit `app.py` and modify the port:

```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change 5000 to desired port
```

### Environment Variables

You can set the Flask environment:

```bash
# On Windows
set FLASK_ENV=production
python app.py

# On macOS/Linux
export FLASK_ENV=production
python app.py
```

## 📝 API Endpoints

### POST /translate

Translates English text to Kannada and generates audio.

**Request:**
```json
{
    "text": "Hello, how are you?"
}
```

**Response (Success):**
```json
{
    "success": true,
    "original": "Hello, how are you?",
    "translated": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
    "audio_url": "/static/audio/output.mp3"
}
```

**Response (Error):**
```json
{
    "error": "Please enter some text to translate"
}
```

## ⚙️ Technical Details

### Backend (Flask)

- Handles translation requests
- Validates input (max 5000 characters)
- Generates MP3 audio files using gTTS
- Returns JSON responses with translated text and audio URL

### Frontend (HTML/CSS/JS)

- Responsive grid layout
- Real-time character counting
- Loading spinner animation
- Error message display
- Audio player controls
- Copy-to-clipboard functionality
- Smooth animations and transitions

## 🐛 Troubleshooting

### Issue: "Connection Error" or "Translation Failed"

**Solution**: Check your internet connection. The application requires internet access for:
- Google Translate API
- gTTS audio generation

### Issue: Audio Not Playing

**Solution**:
1. Check browser audio settings
2. Ensure volume is not muted
3. Try refreshing the page
4. Use a different browser

### Issue: Slow Translation

**Solution**:
1. Check internet connection speed
2. Reduce text length (max 5000 characters)
3. Restart the application

### Issue: Module Not Found

**Solution**:
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

## 🌐 Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+

## 📱 Mobile Support

The application is fully responsive and works on:
- iOS Safari
- Android Chrome
- Android Firefox
- Tablets (iPad, Android tablets)

## 🔐 Security Notes

- Input is validated on the server side
- Maximum 5000 characters per translation
- No sensitive data is stored
- Audio files are generated on-the-fly

## 🎨 Customization

### Change Color Scheme

Edit the CSS variables in `static/style.css`:

```css
:root {
    --primary-color: #2563eb;      /* Change primary color */
    --background: #f8fafc;         /* Change background */
    /* ... other colors ... */
}
```

### Modify Header

Edit the header section in `templates/index.html`:

```html
<h1>🌐 English to Kannada Translator</h1>
<p class="subtitle">Your custom subtitle here</p>
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [googletrans Documentation](https://github.com/ssut/py-googletrans)
- [gTTS Documentation](https://gtts.readthedocs.io/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 📄 License

This project is provided as-is for educational purposes.

## 👥 Contributing

Feel free to fork, modify, and improve this project!

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the code comments
3. Check the console (F12) for error messages

## 🎉 Version History

### v2.0 (Current)
- Redesigned UI with modern gradient
- Added character counter
- Improved error handling
- Added copy-to-clipboard feature
- Better responsive design
- Comprehensive documentation

### v1.0
- Basic translation functionality
- Simple UI
- Audio playback

---

**Made with ❤️ for language learners worldwide**