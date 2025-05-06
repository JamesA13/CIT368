This application is a simple weather forecast retrieval program that provides a user with the expected conditions, high temp, and low temp for the current day and following two days. 

This project's repository serves as a visible history of the concepts learned in CIT368 - Secure Software Development and Testing at Pennsylvania College of Technology. The initial app was uploaded as an ultra-simple API request app with no security or error handling, and has been refactored to address security concerns such as entering a malicious input, or functional problems such as a failed API call.

This application uses the API provided by https://www.tomorrow.io<br/>
A free API key can be obtained by registering at https://app.tomorrow.io/signup<br/>
Please note that free API keys are subject to these rates:<br/>
Requests per second: 3<br/>
Requests per hour: 25<br/>
Requests per day: 500<br/>

Some of the testing of this application involved the use of the "Big List of Naughty Strings", a repository owned by user "minimaxir" at https://github.com/minimaxir/big-list-of-naughty-strings<br/>
The downloaded file resides in the same directory as app.py and is renamed from "blns.txt" to "blns.payloads"

Additonal imported Python packages include:<br/>
requests
time
datetime
re
unittests

Scanning this project with Bearer SAST revealed 0 failures in 88 checks.

Use of this application requires the creation of "config.py" in the same directory as app.py<br/>
Within "config.py" live the following variables:<br/>
    key : string - a string representation of your API key from https://www.tomorrow.io