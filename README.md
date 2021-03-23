# Weatherbot Tutorial (using the latest release of Rasa NLU and Rasa Core)

Rasa NLU and Rasa Core devs are doing an amazing job improving both of these libraries which results in code changes for one method or another. In fact, since I recorded a Wetherbot tutorial,
there were quite a few changes which were introduced to Rasa NLU and Rasa Core. On 21st of May 2019, Rasa 1.0 was released with a lot of changes under the hood. This repo contains the updated weatherbot code compatible with the latest release of Rasa.

## How to use this repo

### Training the NLU model

Train the NLU model by running:  

```rasa train nlu ```

Once the model is trained, test the model:

```rasa shell nlu```


### Training the dialogue model

The biggest change in how Rasa Core model works is that custom action now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` rasa run actions```  

2. Open a new terminal and train the Rasa Core model by running:  

``` rasa train```  
 
3. Talk to the chatbot once it's loaded after running:  
```rasa shell```  


### Starting the interactive training session:

To run your assistant in a interactive learning session, run:
1. Make sure the custom actions server is running:  

```rasa run actions```  

2. Start the interactive training session by running:  

```rasa interactive```  

### Connecting a chatbot to Slack:
1. Configure the slack app
2. Provide the slack configuration tokens in a credentials.yml file  
3. Make sure custom actions server is running  
4. Start the agent by running `rasa run`
5. Start the ngrok on the port 5004  `./ngrok http 5004`
6. Provide the url: https://your_ngrok_url/webhooks/slack/webhook to 'Event Subscriptions' page of the slack configuration.  
7. Talk to you bot.  

### Open rasa
1. start custom action server

2. open new terminal and start rasa x

``` rasa x ```
