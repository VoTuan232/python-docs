
import json
import time
from locust import task, TaskSet, between
from module.Authentication import Authentication
from module.Union import Union
import random
authentication = Authentication
union = Union


class Company(TaskSet):
    wait_time = between(1, 5)

    def __init__(self, parent):
        super().__init__(parent)
        self.token = ''
        self.headers = {}
        self.users = [
            {
                "email": "yumemi@example.com",
                "password": "12345678a"
            },
            {
                "email": "loc.ngo@sotatek.com",
                "password": "1234567890a"
            },
            {
                "email": "loc.ngo+1@sotatek.com",
                "password": "1234567890a"
            }
        ]

    def on_start(self):
        self.token = self.login()
        self.headers = {'x-sendy-session': self.token}

    def on_stop(self):
        self.logout()

    def login(self):
        response = self.client.post("/authentication/login",
                                    json=random.choice(self.users))
        return json.loads(response._content)['token']['accessToken']

    def logout(self):
        self.client.headers = self.headers
        self.client.post("/authentication/logout")

    def listCompanies(self, code):
        self.client.headers = self.headers
        response = self.client.get(
            '/unions/' + code + '/companies')
        return json.loads(response._content)

    def createCompany(self, code):
        self.client.headers = self.headers
        self.client.post("/unions/" + code + '/companies', json={
            "companyName": str(time.time()) + "アイアジア国際交流協同組合",
            "companyNameKana": "おおさかじょう",
            "representativeName": "羽柴秀吉",
            "zipcode": "1000000",
            "address": "東京都足立区以下に掲載がない場合",
            "phone": "0123-4444-4444",
            "fax": "0123-4444-4444",
            "email": "test@example.com",
            "industryType": "業種"
        })

    def getCompanyDetail(self, code, companyId):
        self.client.headers = self.headers
        response = self.client.get(
            '/unions/' + code + '/companies/' + companyId)
        return json.loads(response._content)

    def editCompanyDetail(self, code, companyId):
        self.client.headers = self.headers
        self.client.patch(
            '/unions/'+code+'/companies/'+companyId, json={
                "companyName": str(time.time()) + "アイアジア国際交流協同組合",
                "companyNameKana": "おおさかじょう",
                "representativeName": "羽柴秀吉",
                "zipcode": "1000000",
                "address": "東京都足立区以下に掲載がない場合",
                "phone": "0123-4444-4444",
                "fax": "0123-4444-4444",
                "email": "test@example.com",
                "industryType": "業種"})

    def deleteCompany(self, code, companyId):
        self.client.headers = self.headers
        self.client.delete('/unions/' + code + '/companies/' + companyId)

    @task
    def company(self):
        listUnions = union.listUnion(self)
        code = listUnions[random.randrange(0, len(listUnions))]['code']
        self.createCompany(code)
        listCompanies = self.listCompanies(code)
        companyId = listCompanies['items'][0]['id']
        self.getCompanyDetail(code, companyId)
        self.editCompanyDetail(code, companyId)
        self.deleteCompany(code, companyId)
