# HermesBot :cowboy_hat_face:

<p align="center"> 
A <a href="https://rasa.com/">Rasa</a>-based chatbot that translates text from English to several other languages using the 
  <a href="https://pypi.org/project/translate/">translate</a> Python module. 
  Rasa uses a Dual Intent and Entity Transformer (DIET) for NLP/NLU and trains using min-min and min-max algorithms. HermesBot also uses memoization and rule-based policies. In addition to the translate module, I also included an emoji package so it's a little more fun to interact with :zany_face:
</p>

## Run the bot  
Since Rasa x is no longer free, you can speak to it on the command line by running 
`rasa run actions` and `rasa shell`on separate terminals. 

## Testing 
In tests, it can identify commands pretty well. Check out the confusion matrix with `rasa test`. The failed tests and other info is in the results folder.

## Visualization 
Take a look at the flow of conversation: 
 <p align="center">
<img src="https://user-images.githubusercontent.com/84393679/218781894-d4dcb9f8-a9f1-4cf1-a449-4d4141aaea3e.png" width=500 height=500>
</p>

You can see this a little clearer in graphs.html.

## Telegram
 Rasa makes it pretty easy to connect to other voice and chat platforms. Here it is as a telegram bot: 
<p align="center">
<img src="https://user-images.githubusercontent.com/84393679/218571208-0d7a5cfe-2909-40a2-9092-e6ccb3877917.png" width=300 height=700>
</p>

### Connect to Telegram
Run `ngrok http 5005` to obtain secure remote URL. Use this for webhook_url in credentials.yml file. 

Fill out the other sections by contacting @BotFather on telegram and setting up a new bot. 

Make sure to comment out the rasa localhost url in credentials.yml 

