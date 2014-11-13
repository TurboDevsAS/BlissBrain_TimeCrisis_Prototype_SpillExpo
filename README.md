Intro
========

Current version: Prototype 0.0.1 Alpha for Windows

This prototype of BlissBrain was made for SpillExpo, Norways largest gaming expo.
It was specifically designed to show developers how a Emotiv EEG headset can be connected to almost anything using a USB relay.
We choose to connect the emotiv to a Playstation 1, through a light-gun used in games such as Time Crisis.

Hardware needed
========

* [Emotiv EEG headset.](http://emotiv.com/)
* [USB Relay.](http://www.ebay.com/itm/251395571994)
* Playsation 1 (or 2).
* A light-gun that uses a pedal connected to the gun with either 3.5mm jack, RJ9 or anything else that has 2 wires.
* A game, like time crisis.

Dependencies
========

* [Emotiv SDK lite.](http://emotiv.com/store/product_262.html)
* [Emotiv Control Panel.](http://emotiv.com/store/product_72.html)
* [Python 2.7.7 32bit.](https://www.python.org/)
* [Kivy 1.8.0 32bit.](https://www.python.org/)
* [PyEpoc.](https://github.com/dplass/PyEpoc)

Installation
============

1. install emotiv control panel and emotiv sdk lite.
2. copy all the files from ```Emotiv SDK v2.0.0.20-LITE/dll/32 bit``` into ```Emotiv EPOC Control Panel v2.0.0.20/Applications```.
3. copy ```BlissBrain_TimeCrisis.py```, ```blank.png```, ```crouch.png``` and ```stand.png``` into ```Emotiv EPOC Control Panel v2.0.0.20/Applications```.
4. copy ```usb_relay_device.dll``` that you got from the ebay-seller of the usb-relay into ```Emotiv EPOC Control Panel v2.0.0.20/Applications```.
5. download the wrapper PyEpoc from:
[https://raw.githubusercontent.com/dplass/PyEpoc/master/PyEpoc.py](https://raw.githubusercontent.com/dplass/PyEpoc/master/PyEpoc.py) and place it into ```Emotiv EPOC Control Panel v2.0.0.20/Applications```.

Add the dll folder to your Environmental Variables by right-clicking “My computer”, select “properties”, then “advanced” and then “Enviroment variables”.

Select the “Path” variable under “system variables”, then click the “Edit…” button and add the path to your dll folder in the Emotiv SDK lite.

For example:

```;C:/Program Files (x86)/Emotiv SDK v2.0.0.20-LITE/dll```


That's it!


Training and BlissBrain background
============

If you already own a Emotiv headset, you probably know how to visualise and train the cube moving up and down.
Although this method will work, we recommend a different approach, based on our own research and experience.

The concept of BlissBrain is that you don't visualise an object (the cube) moving up or down while you train the thought-command in the Control Panel.
Rather than visualising the movement of an object, we recommend that you visualise a symbol or even a picture in your head while you train the thought-command in the control panel.

We got the idea from research done with fMRI scanners, where the same brain-activity occurred both when a test-subject saw an image and when the test-subject visualised the same image later.

This research was presented by [Mary Lou Jepsen in a TED-talk last year](https://www.ted.com/talks/mary_lou_jepsen_could_future_devices_read_images_from_our_brains).

The complete study can be read here:
[Brain areas underlying visual mental imagery and visual perception: an fMRI study](http://www.wjh.harvard.edu/~kwn/Kosslyn_pdfs/2004Ganis_CogBrainRes20_BrainAreas.pdf)

In our own research, using the Emotiv EEG headset, we asked the test-subjects to visualise the symbols " + " and " - " while we trained the tought-commands for "lift" and "drop" in the Emotiv Control Panel.

While we trained the symbols " + " and " - ", we displayed the symbols in full-screen on a different device to make it easier for the test-subject to focus on the symbol.
This was also the method we used at SpillExpo, where over 17,000 people came, and around 500 got the chance to play around with this prototype.
The people who tried it needed to train "neutral", "lift" and "drop" 3-5 times for them to have control.

Instructions for training using symbols:

1. on a different screen/device, display a symbol like " + " or " ↑ " or whatever you want.
2. while the test-subject is focusing on the symbol and visualising the symbol in his/her head, train the "lift" command in the Emotiv control panel.
3. repeat for the "drop" command in the Emotiv contorl panel, but this time, use a different symbol like " - " or " ↓ "

Instructions for training without symbols:
1. train "lift" and "drop" in the Emotiv Control Panel like usual.

Setup hardware:
============

It doesn't matter what type of plug you have for your playstation light-gun, as long as it has a pedal with a cable that only has two wires.
For this guide, we are using a "REAL ARCADE LIGHT GUN" that has a old telephone-jack (RJ9).

Rather than destroying the pedal, take a standard RJ9 to RJ9 cable (or if your light-gun has a 3.5mm jack, take a 3.5mm jack to 3.5mm jack cable) and chop of the other end.
Now you have a long RJ9 with 2 wires sticking out of the other end.
Connect these two wires to the usb-relay (positive and negative inputs).

Done!

Playing:
============

If you have everything setup and the cube in the control panel is moving up/down when you're visualising the symbols you selected, you can start the "BlissBrain_TimeCrisis.py" script.

A window should appear, displaying a solider with a gun either standing or crouching depending if you're thinking about the symbol for "lift" or "drop".

You should also hear a clicking noise from the usb-relay, and see the red-light on the usb-relay switch between on and off whenever you switch between "lift" and "drop".
While playing your preferred light-gun game, simply think about the symbol for "drop" to activate the "pedal", and think about the symbol for "lift" to deactivate the "pedal".
Usually, activating the pedal means that you are crouching in the game, but some games may utilize the pedal differently.

Have fun!


Authors
=======
TurboDevs AS and Larsen Development.

Tobias Andersen, Sigve Larsen, Nine Bauge, Jan Ole Lysen Andersen, Emilie Thomassen, Raymond Holthe.

[![DOI](https://zenodo.org/badge/4893/TurboDevsAS/EEGBliss.png)](http://dx.doi.org/10.5281/zenodo.10700)

