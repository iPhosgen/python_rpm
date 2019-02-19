##python_rpm

This is a simple template for general Python project that you may pack to RPM distribution package.

###Requirements

For build RPM packeges you need to install `rpm` on your machine

`sudo apt install rpm`

###How it use

For building distribution package (for example RPM) from your code run following commads:

`cd python_rpm`
`python3 -m venv env`
`source env\bin\activate`
`pip install --upgrade pip`
`pip install -r requirements.txt`
`python3 setup.py bdist --format=rpm`
