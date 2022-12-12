import gc
from datetime import datetime, timezone
import pandas as pd
from flask import Flask, request
from flask_restx import Resource, Api, fields
import json, random
from dateutil.tz import gettz
# from controller import classes_and_functions as cf

flask_app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace("Secret-Santa", description="Want to Know whom you will surprise this Christmas, lets find out!")

@name_space.route("/get_person_name/<your_name>")
class SecretSanta(Resource):
    '''Secret Santa'''

    def get(self, your_name):
        '''GET API'''
        list_emp = ['shuchi.trivedi@kibbcom.com', 'sumit.joshi@kibbcom.com', 'neeta.wadawadgi@kibbcom.com', 'shelly.pritchard@kibbcom.com', 'jeevanmd@kibbcom.com', 'shalini.gupta@kibbcom.com', 'istaque.hussain@kibbcom.in', 'sajeev.manikkoth@kibbcom.com', 'akash.mahale@kibbcom.com', 'shailja.sharma@kibbcom.com', 'mukesh.kumar@kibbcom.com', 'nitesh.rathore@kibbcom.com', 'nisar.ahmed@kibbcom.com', 'amit.singh@kibbcom.com', 'vivek.gupta@kibbcom.com', 'Khushboo.pandey@kibbcom.com', 'magesh.vasudevan@kibbcom.com', 'rahul.mishra@kibbcom.com', 'nisar.sheikh@kibbcom.com', 'shaik@kibbcom.com', 'basavaraj.tenginakai@Kibbcom.com', 'nisha.sinha@kibbcom.com', 'balu.goudi@kibbcom.com', 'vikasmd@kibbcom.com', 'prem.prakash@kibbcom.com', 'Komali.Pasumarthy@Kibbcom.com', 'nikitha.mahale@kibbcom.com', 'sumit.gupta@kibbcom.com', 'anila.m@kibbcom.com', 'niteshr@kibbcom.com']
        dictionary = json.load(open('employees.json','r'))
        dictionary_receive = json.load(open('receivers.json','r'))
        allocated = json.load(open('allocated.json','r'))
        time_now = datetime.now(tz=gettz('Asia/Kolkata'))

        with open('logs.txt','a') as logs:
            logs.write(f'{your_name} tried at {time_now}\n')
        # print(your_name, " tried at ", time_now)

        sender_list = list(dictionary.keys())
        receiver_list = list(dictionary_receive.keys())
        allocated_list = list(allocated.keys())

        sender = your_name
        if sender in allocated_list:
            return {
                'message':'You very chalank bro!'
            }
        if sender not in list_emp:
            return {
                'message':"Wrong email address!"
            }
        temp_list = [emp for emp in receiver_list if emp!=sender]
        receiver = random.choice(temp_list)
        done = {}
        done[sender] = receiver

        print(sender," is ",receiver,"'s Secret Santa.\n") 
        data = {}
        with open('allocated.json','r') as file:
            data = json.load(file)
            data[sender]=receiver

        with open('allocated.json','w') as file:
            json.dump(data,file)

        del dictionary[sender]
        del dictionary_receive[receiver]

        with open('employees.json','w') as file:
            json.dump(dictionary,file)

        with open('receivers.json','w') as file:
            json.dump(dictionary_receive,file)
        return {'message':f'{sender}, you will surpise {receiver} this Christmas!'}