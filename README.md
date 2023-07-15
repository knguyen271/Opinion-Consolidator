# Opinion-Consolidator
## What Is The Opinion Consolidator
The Opinion Consolidator is a program that finds the opinions regarding the wanted topic. It then analyzes the data and puts it in terms of text and graphs for the user to understand. 

## Instructions
### **Download the required environments from the ["requirements.txt"](https://github.com/knguyen271/Opinion-Consolidator/blob/main/requirements.txt) file**

Run the file called "main.py" and wait for the GUI to show up. When the GUI shows up, input the wanted topic in the textbox instructed and click the submit button. The consolidator then looks for comments about the topic and after a minute it gives the data in graphs and text.  

The GUI may go unresponsive while searching for the comments, but the program is still running. 

## How Does It Work?
Once the program gets the topic from the user, it uses Selenium Webdriver to open a chrome brower. Once the chrome brower is open, it goes to YouTube and looks for the topic and gets the most relevant videos on the topic. The program, still using Selenium Webdriver, collects the top comments from the video and adds it to an array. Each comment is later cleaned, removing emojis, fixing spelling errors, etc., and using TextBlob polarity scorer, it rates each comment. The score of 0 means that the comment is neutral, a negative rating means that the comment is negative and a positive rating means the comment is positive. The polarity is then graphed as well as the frequency of words and shown to the user. 

## Contributor
This project was made by Ken Nguyen. If there are any questions email this address.
Email : ken.nguyen160816@gmail.com
