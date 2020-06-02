# Amazon-Pricker-Tracker :mag: [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama) [![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 


It notify in your Window Notification Panel as price get low as you want
<img src="https://github.com/heykush/Amazon-Price-Tracker/blob/master/InkedAmazon-price-tracker_LI.png" align="center" />

# DEMO
## Using .py Script
![demo](https://github.com/heykush/Amazon-Price-Tracker/blob/master/ezgif.com-gif-maker%20(1).gif?raw=true)

## Using .exe file
![demo](https://github.com/heykush/Amazon-Price-Tracker/blob/master/ezgif.com-gif-maker%20(2).gif?raw=true)

 ## Installation
1. **Clone the repo**
```sh
git clone https://github.com/heykush/Amazon-Price-Tracker.git
```
2. Install packages
 **Must to install**
 Copy the below commands and Run in `bash/cmd` terminal one at a time. 
 ~~~
 pip install requests
 pip install plyer
 pip install time
 pip install beautifulsoup4
~~~
## Convert *.py to .exe*
**Run in terimal**
~~~
pyinstaller --hidden-import plyer.platforms.win.notification -F -w -i "give image path" amazontacker.py
~~~
## NOTE : 
***Your image should be in .ico format.*** **[Convert](https://image.online-convert.com/convert-to-ico) Jpeg, png to icon.**
<!-- USAGE EXAMPLES -->
## Usage
You can use this as script or run as .exe in your window. You can **customized** the **link of product** , Your **willing price and Time gap between every notification.**


Contributing
==========
Any kind of contributions are welcome.
1. **Fork** the repo on GitHub.
2. **Clone** the project to your own machine.
3. **Commit** changes to **development** branch.
4. **Push** your work back up to your fork.
5. Submit a **Pull request** so that I can review your changes

## Contact

Gaurav Kushwaha - [@ravvkush](https://instagram/ravvkush) - gkush10000@gmail.com


## License & Copyright
© [Gaurav kushwaha](https://heykush.github.io/)

Licensed under the [MIT License](License)
