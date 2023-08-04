import slack
import requests
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from flask_restful import Api,Resource
app = Flask(__name__)
api =Api(app)
slack_event_api = SlackEventAdapter('6e759bbe36cd3532205c0729cd53e1a5' , '/slack/events', app)
#k

client =slack.WebClient(token='xoxb-5679288130871-5693863167794-ppzuG4iELTfp2JIaJB7FkrxX')

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

