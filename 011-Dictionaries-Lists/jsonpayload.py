
student_info = {
    "name": "manoj",
    "age": "32", 
    "exp": "10years",
    "cloud": "aws" 
}

print(student_info)

server_info = [
    {
        "name": "catalogue",
        "disk": "30", 
        "type": "t3.micro",
        "cloud": "aws" 
    },
    {
        "name": "cart",
        "disk": "50", 
        "type": "t3.medium",
        "cloud": "gcp" 
    },
    {
        "name": "user",
        "disk": "40", 
        "type": "t3.micro",
        "cloud": "ali" 
    }
]

print("Printing Component Info:", server_info[0])
print("Printing Component Cloud:", server_info[0]["cloud"])