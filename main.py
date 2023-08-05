import slack
import requests
from dotenv import load_dotenv
import os
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from flask_restful import Api,Resource
load_dotenv('.env')
slack_web_token=os.getenv('SLACK_WEB_TOKEN')
slcak_signing_secret = os.getenv('SLACK_SIGNING_SECREAT')
print(slack_web_token)
app = Flask(__name__)
api =Api(app)
slack_event_api = SlackEventAdapter(slcak_signing_secret , '/slack/events', app)
#k

client =slack.WebClient(token=slack_web_token)

# @slack_event_api.on('message')
# def message(payload):
#     event = payload.get('event',{})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#
#     text = event.get('text')
#     print(text)
#     client.chat_postMessage(channel=channel_id,text=text)



class Check(Resource):
  def post(self):
      print(request.json['question'])
     # r=requests.post('  https://f9c3-202-8-112-91.ngrok-free.app/Ai/askQuestion', json ={'question':request.json['question']})
      # print(r.json()['answer'])
      client.chat_postMessage(channel='#test', text='hello')
      return {'message':'success'}

api.add_resource(Check,'/get')

if __name__ == "__main__":
    app.run(debug=True)

