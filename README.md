This application is a simple weather forecast retrieval program that provides a user with the expected conditions, high temp, and low temp for the current day and following two days. 

This project's repository serves as a visible history of the concepts learned in CIT368 - Secure Software Development and Testing at Pennsylvania College of Technology. The initial app was uploaded as an ultra-simple API request app with no security or error handling, and has been refactored to address security concerns such as entering a malicious input, or functional problems such as a failed API call.

This application uses the API provided by https://www.tomorrow.io 
A free API key can be obtained by registering at https://app.tomorrow.io/signup 
Please note that free API keys are subject to these rates: 
Requests per second: 3 
Requests per hour: 25 
Requests per day: 500 

Some of the testing of this application involved the use of the "Big List of Naughty Strings", a repository owned by user "minimaxir" at https://github.com/minimaxir/big-list-of-naughty-strings 
The downloaded file resides in the same directory as app.py and is renamed from "blns.txt" to "blns.payloads"

Use of this application requires the creation of "config.py" in the same directory as app.py 
Within "config.py" live the following variables: 
    key : string - a string representation of your API key from https://www.tomorrow.io