import slack
import requests
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from flask_restful import Api,Resource
app = Flask(__name__)
api =Api(app)
slack_event_api = SlackEventAdapter('e435a3403c117be73a76c7588aa5aaaa' , '/slack/events', app)
#k

client =slack.WebClient(token='xoxb-5674230910401-5664059319844-ygtH0xJgAyr3S7nvdg0qTb3H')

@slack_event_api.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')

    text = event.get('text')
    print(text)
    client.chat_postMessage(channel=channel_id,text=text)



class Check(Resource):
  def post(self):
      print(request.json['question'])
     # r=requests.post('  https://f9c3-202-8-112-91.ngrok-free.app/Ai/askQuestion', json ={'question':request.json['question']})
      # print(r.json()['answer'])
      client.chat_postMessage(channel='#gopro', text='hello')
      return {'message':'success'}

api.add_resource(Check,'/get')

if __name__ == "__main__":
    app.run(debug=True)

