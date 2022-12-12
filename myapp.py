import gc
from datetime import datetime, timezone
import pandas as pd
from flask import Flask, request
from flask_restx import Resource, Api, fields
import json, random
# from controller import classes_and_functions as cf

flask_app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace("Secret SAnta", description="Want to Know whom you will surprise this Christmas, lets find out!")

@name_space.route("/get_person_name/<your_name>")
class SecretSanta(Resource):
    '''Secret Santa'''

    def get(self, your_name):
        '''GET API'''
        dictionary = json.load(open('employees.json','r'))
        dictionary_receive = json.load(open('receivers.json','r'))
        allocated = json.load(open('allocated.json','r'))
        time_now = datetime.now()

        with open('logs.txt','a') as logs:
            logs.write(your_name, " tried at ", time_now)
        # print(your_name, " tried at ", time_now)

        sender_list = list(dictionary.keys())
        receiver_list = list(dictionary_receive.keys())
        allocated_list = list(allocated.keys())

        sender = your_name
        if sender in allocated_list:
            return {
                'message':'You very chalank bro!'
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