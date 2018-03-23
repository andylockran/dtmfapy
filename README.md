# Introduction

This is the python repo that listens to DTMF tones and prints them out.


## Setup

Install portaudio
`brew install portaudio`

Install virtualenv
`pip install virtualenv`
Setup your virtualenv for this project:
`virtualenv --python python2.7 venv/`
Activate it
`source venv/bin/activate`
Install requirements:
`pip install -r requirements.txt`

## Testing

Run the DTMF parsing tests (run against the file audio/output.wav)
`python -m pytest tests/`

If you add your files to audio/ with the filename '${expectedcode}.wav' - then the tests will pick them up.

## Run the app

`python dtmfa/app.py`
