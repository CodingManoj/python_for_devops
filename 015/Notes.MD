We have python script ready that can create a JIRA Ticket.
What we needto do is, when some placed /create on COMMENT of the GitHub issue, it should create a JIRA

Flow :  Github talking to APP's API ---->  (Python app running EC2 )  ----> APP talking to Jira and creating a ticket
Supply the Application URL of the python in the webhooks section of the repo.

Flask is a python framework that's offered to created Web Based Python Applications.

# Let's understand 
1) What is API 
2) Convert Python Script that you wrote to Python API
3) Deploy Script To Server
4) So, that GITHUB can invoke script with an API
5) Conditionalize, so that only specific keyWors on comments of the issue can fire Jira. ( If payload has /jira, then only create ISSUE)

## We will write an API using Flask Framework.

github.com is the GitHub's UI,
api.github.com is the application interface of GitHub.
Application talking to another applications can be done easy with the help of API's.


What are the different types of API's ? Typically all of these works on http 
there are 4 types of http reqeusts :
    1) POST         ( Creates record )    
    2) PUT          ( Updates record )
    3) DELETE       ( Deletes record )
    4) GET          ( Fetches record )
In our case, GITHUB has to POST a reqest to APPLICATION.
    
With Flask, writing API's is quick and it's even easy to convert our script to API.
## How to write a FLASK API ? first install flask on your computer
pip install flask




