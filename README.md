# netflixselenium

Welcome! This is just a simple project where I automate basic Netflix functionality via Selenium.

# Setup

The first thing you'll need to do is create a my_secrets.py file in the root directory. This file should contain the following lines:

```
MY_CHROMEDRIVER_PATH = "type your chromedriver path here"
MY_EMAIL = "type your email here"\
MY_PASSWORD = "type your password here"
PREFERRED_USER = ""
```

In `MY_EMAIL`, you should type the email for your Netflix login. 

In `MY_PASSWORD`, type the password you use during your Netflix login.

If you have multiple users (for instance, if you share your Netflix account with other people), you can specify a `PREFERRED_USER`. Make sure to type your preferred user's name as accurately as possible, as it is case-sensitive. 

If you do not share your Netflix account with anyone else, you can leave `PREFERRED_USER` as is.

Next, we'll look into the chrome driver setup.

## For Linux

Notice that I did this entire process on an Ubuntu distribution of Linux, (it was actually the Windows Subsystem for Linux 2 (WSL2)). Though that should't really matter, I've definitely ran into issues whilst trying to setup the dependencies for this project. Regardless; just follow the commands below, and you *should* be fine.
```
mkdir tmp
cd tmp
mkdir driver
cd driver
sudo apt install wget # If you don't have it already
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Make sure your installation worked with

`chromedriver --version`

If you had previously used chromedriver, run `which chromedriver` and make sure the output is `/usr/bin/chromedriver`.

For Linux, you do have to have Chrome installed. Assuming you completed the steps above, this can be done via:

```
cd tmp
mkdir chrome
cd chrome
sudo apt update
sudo apt upgrade
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
```

Then type google-chrome to see if it all works.

Once you have your chromedriver and chrome installed, you can change the `MY_CHROMEDRIVER_PATH` of the my_secrets.py file to `"/usr/bin/chromedriver"`.

## For Windows

Though I never attempted to do this in Windows, theoretically all you need to do is to download the correct version of the driver from this [website](https://chromedriver.chromium.org/downloads).

To know which version you need, type `chrome://version/` into your Chrome browser (assuming you have that installed. If you don't, install it). Should be the first line you see in that page.

Then place the downloaded chromedriver into a folder you like, and copy the path of that folder into `MY_CHROMEDRIVER_PATH`, in the my_secrets.py file. Make sure you add an "r" before the string, so it'll be something like

`r'C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe'`

## For MacOS

TDB

## Creating a virtual environment and installing selenium

The only piece missing from this dependency puzzle is the selenium package. You can easily download it via

`pip install selenium`

that is, assuming you have python and pip. 

It is also good practice to create a python virtual environment, and only install selenium in that environment. You can create one via

`python -m venv /path/to/new/virtual/environment`

though you do need to install something in `apt` in order to do that. I will add that to this README.md once done.

# Usage

In main.py you'll find a sample of what is currently possible with this project.

We start by importing a `Netflix()` class and creating an object of that class.
Then, you should be able to do `n.watch("query")`, and if all is set up correctly selenium will open a new instance of Chrome, login to Netflix, search for your query, and play the best match for it. Try running `python main.py` to see it for yourself.

Have fun!
