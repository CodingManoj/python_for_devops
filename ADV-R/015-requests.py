import requests

info=requests.get('https://gitlab.com/thecloudcareers/opensource/-/raw/master/lab-tools/ansible/install.sh')
print(info)