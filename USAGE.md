# Quick Start Guide - English to Kannada Translator

## 🚀 Getting Started in 5 Minutes

### Step 1: Open Terminal/Command Prompt

Navigate to the project folder:
```bash
cd english_to_kannada_translator
```

### Step 2: Activate Virtual Environment

**On Windows:**
```bash
env\Scripts\activate
```

**On macOS/Linux:**
```bash
source env/bin/activate
```

### Step 3: Start the Application

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 4: Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

## 💡 How to Use

### Basic Translation

1. **Type or paste English text** in the textarea
   - Maximum 5000 characters
   - Real-time character counter shown below

2. **Click "Translate & Play" button**
   - Or press **Ctrl + Enter** for quick access

3. **Wait for translation** (usually 2-5 seconds)
   - Loading spinner will show during processing

4. **View results:**
   - Original English text displayed
   - Kannada translation shown below
   - Audio player automatically plays pronunciation

### Copy Translation

1. Click the **"Copy Translation" button**
2. Text is copied to your clipboard
3. Paste it anywhere with Ctrl+V (or Cmd+V on Mac)

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + Enter | Quickly translate |
| Ctrl + C | Copy (after translation) |

## 🎨 UI Features

- **Character Counter**: Shows how many characters you've typed (max 5000)
- **Error Messages**: Clear error descriptions if something goes wrong
- **Loading Spinner**: Visual feedback while translating
- **Audio Player**: Controls to play/pause/adjust volume
- **Responsive Design**: Works on mobile, tablet, and desktop

## ❌ Troubleshooting

### App won't start
```bash
# Make sure you're in the right directory and have activated venv
pip install -r requirements.txt
python app.py
```

### "Address already in use" error
The app is already running on port 5000. Stop it (Ctrl+C) or change the port in app.py.

### Audio not playing
- Check your browser's audio settings
- Make sure your volume isn't muted
- Try refreshing the page

### Translation takes too long
- Check your internet connection
- Try with shorter text
- Restart the application

## 🛑 Stopping the Application

Press **Ctrl + C** in the terminal where the app is running.

## 📝 Example Usage

### Input:
```
"Hello, I am learning Kannada language. This is very interesting."
```

### Output:
```
Kannada: "ನಮಸ್ಕಾರ, ನಾನು ಕನ್ನಡ ಭಾಷೆ ಕಲಿಯುತ್ತಿದ್ದೆ. ಇದು ತುಂಬಾ ಆಸಕ್ತಿದಾಯಕವಾಗಿದೆ."

Audio: [Plays Kannada pronunciation]
```

## 📱 Mobile Usage

1. Find your computer's IP address:
   - Windows: Open Command Prompt, type `ipconfig`
   - Mac/Linux: Open Terminal, type `ifconfig`

2. Look for "IPv4 Address" (usually looks like 192.168.x.x)

3. On your mobile device, go to:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

4. Use the translator as normal!

## 🔄 Common Tasks

### Translate multiple texts
- Clear the textarea
- Enter new English text
- Click translate again

### Change text size (zoom)
- Use browser zoom: Ctrl + Plus (+)
- Reduce zoom: Ctrl + Minus (-)
- Reset: Ctrl + 0

### Save translations
- Click "Copy Translation" button
- Paste into a text editor or Word document
- Save as needed

## 🎯 Tips for Best Results

1. **Use clear, simple sentences** - Works better than complex text
2. **Keep text moderate** - Under 500 characters for fastest results
3. **Check audio pronunciation** - Review if translation sounds correct
4. **Internet required** - Always have internet connected
5. **Modern browser** - Use Chrome, Firefox, Safari, or Edge

## 📞 Need Help?

1. Check the **README.md** for detailed documentation
2. Review error messages (they're quite descriptive)
3. Check browser console (F12) for technical errors
4. Restart the application if something seems stuck

---

**Happy translating! 🎉**

python translate_tts.py --file input.txt --out output_kn.mp3
```

Notes
- The script uses `googletrans` (free/unofficial) for translation and `gTTS` for speech.
- On Windows the generated MP3 will be opened by the default audio player.
- If playback does not start automatically, open the MP3 file manually.

Want a GUI or web interface? Ask and I can add a small Flask app or desktop UI.
