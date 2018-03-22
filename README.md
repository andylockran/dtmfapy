# Introduction

This is the python repo that listens to DTMF tones and prints them out.


## Setup


Install virtualenv
`pip install virtualenv`
Setup your virtualenv for this project:
`virtualenv --python python2.7 venv/`
Activate it
`venv/bin/activate`


## Testing

Run the DTMF parsing tests (run against the file audio/output.wav)
`python -m pytest tests/`


