# from fastapi import FastAPI
# from pydantic import BaseModel
# import random
# import json

app = FastAPI(description='Secret Santa',title='Wondring whom you will surprise this Christmas, lets find out!')

# dictionary = json.load(open('employees.json','r'))
# dictionary_receive = json.load(open('receivers.json','r'))
# allocated = json.load(open('allocated.json','r'))

# sender_list = list(dictionary.keys())
# receiver_list = list(dictionary_receive.keys())
# allocated_list = list(allocated.keys())

@app.get("/santa/{yourName}")
def get_app(your_name:str):
    dictionary = json.load(open('employees.json','r'))
    dictionary_receive = json.load(open('receivers.json','r'))
    allocated = json.load(open('allocated.json','r'))

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