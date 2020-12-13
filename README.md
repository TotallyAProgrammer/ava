# Ava
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FTotallyAProgrammer%2Fava.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FTotallyAProgrammer%2Fava?ref=badge_shield)


## An adVanced Assistant

Ava is my new personal assistant.
My goal is to have an advanced assistant that will be just as capable as most modern personal assistants such as Alexa, Bixby, Google, and Siri.
I am choosing to make my own to decrease the tracking done on me and my data.

### Development

Due to AVA being ever-evolving it is _highly_ reccomended that you work in a python virtual environment (venv).
AVA has been tested to function with Python 3.6.8 and above, it is strongly reccomended to work with the latest python version regardless.
AVA has only been tested to function with the versions of the used libraries listed in the requirements.txt, but it should work in newer versions of them too.

### Requirements

AVA Relies on the following versions (or higher) for full functionality:
Many of these are dependencies.

- pyttsx3 2.90
- SpeechRecognition 3.8.1
- pocketsphinx 0.1.15
- wikipedia 1.4.0
- pyaudio 0.2.11
- beautifulsoup4 4.9.3
- certifi 2020.12.5
- chardet 3.0.4
- idna 2.10
- requests 2.25.0
- soupsieve 2.0.1
- urllib3 1.26.2

__Note on pyttsx3 and eSpeak-NG__
In order to use eSpeak-NG as your TTS engine, you may have to build from source, as a release with support may not have been released yet.

### Known Possible Issues

- Building SpeechRecognition is a pain because of PyAudio. <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>
- Building PocketSphinx is a pain. You'll need:
  - pulseaudio-libs-devel
  - alsa-lib-devel
  - swig
  - gcc
  - python3x-devel (Where x is your version)
- Currently AVA doesn't run on well on linux due to pyttsx3 2.90 and prior not having espeak-ng support built in (This is fixed with PR #163)


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FTotallyAProgrammer%2Fava.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FTotallyAProgrammer%2Fava?ref=badge_large)