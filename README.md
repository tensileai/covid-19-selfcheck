# Covid-19 Self-Assessment Decision Tree

Open-source self-assessment tool focused on individuals without access to internet or smartphones

Tensile AI has open-sourced code, based on CDC guidelines, to enable organizations to develop COVID-19 self-assessment applications focusing on individuals without access to internet or smartphones. Many tools have been developed since the outbreak of the pandemic to help individuals assess their symptoms and determine if they are a candidate for a COVID-19 test. These require smartphone or internet access. Recognizing the vulnerability and risk in populations that lack connectivity, we are offering our code as a quick-start to organizations looking to implement assessment tools for this segment of the population. We envision applications that allow an individual to interact with a Bot to help determine whether he/she is vulnerable to COVID-19, and if so, obtain information on his/her best course of action for getting tested. While we created this code for the current COVID-19 crisis, we hope that if a future health crisis arises, it can serve as an implementation primer when time, especially for these populations, is of the essence. 

## main.py

The main code is a dialog of questions and answers leading to guidance if an individual should seek medical care or stay home therefore avoiding the ER.  The decision path is based on the CDC self checker template. The intent of this module is to provide a starting point for implementing a text or speech based self-assesssment software solution.

## Integration with Speech Recognition, Speech to Text, and Voice activated responses

The file main.py is a basic template for a command line interface (CLI) and can be run with Python 3.

An interactive version, main_voice.py, is also provided using Google Speech Recognition and Text To Speech.  To install these pacckages, run these steps:

```python
pip install SpeechRecognition
pip install gTTS
pip install pipwin
pipwin install pyaudio
```

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details
