# Water Drinking Notification App

Hello there! This is a simple yet effective Python application designed to remind you to stay hydrated throughout the day. 

## About

The application uses the `plyer` module in Python to send desktop notifications every hour. The notification gently reminds you to drink water and provides a brief note on the recommended daily fluid intake.

## How it Works

The script runs an infinite loop, where each iteration does the following:

1. Sends a notification with the title "Please Drink Water Now!!".
2. The message in the notification reads: "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women."
3. The notification displays an icon from a specified path.
4. The notification stays on the screen for 12 seconds.
5. The script then goes to sleep for an hour before the next iteration starts.

## Setup

To run this application, you need Python installed on your system. If you don't have Python installed, you can download it from the official site.
