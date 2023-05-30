# Fund_That_Flip

Project Requirements : 

APIs are like snowflakes, no two are alike. The data team will have to integrate with various 3rd party APIs to gain access to our data. NeoWs is
an API provided by NASA to locate near-earth objects. The feed serves up a paginated list of near-earth objects based on a start and end date.

● API documentation and access tokens can be obtained here: https://api.nasa.gov/

Using Python/Ruby, write an API that pulls a list of NEOs from the feed route provided by the service. The application should meet the following
requirements:

● Data should be stored in a database (SQL or NoSQL)

● The application should pull data with a start date of 1982-12-10

● The application should convert all epochs to an ISO8601 timestamp (GMT)

● The application should only store imperial measurements (feet, miles)

● The application should treat the neo_reference_id as PII storing only the last 4


To run this, cd into desired directory and run "git clone <repository_url>"

You will need to have python installed on your computer. 

-Run pip install requests

From that directory run python main.py and a sqlite file will be created in same directory as where the script is stored. 
