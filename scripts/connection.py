import cohere
from cohere.classify import Example
import os
from dotenv import load_dotenv
load_dotenv()
co = cohere.Client(os.getenv("API_TOKEN"))
response = co.classify(
  inputs=["this movie was great", "this movie was bad"],
  examples=[
    Example("love this movie", "positive review"),
    Example("I would watch this movie again with my friends", "positive review"),
    Example("I would watch this movie again", "positive review"),
    Example("i liked this movie", "positive review"),
    Example("this is my favourite movie", "positive review"),
    Example("worst movie of all time", "negative review"),
    Example("I would not recommend this movie to my friends", "negative review"), 
    Example("I did not want to finish the movie", "negative review"),
    Example("hate this movie", "negative review"),
    Example("we made it only a quarter way through before we stopped", "negative review"),
    Example("this movie was okay", "neutral review"),
    Example("this movie was neither amazing or terrible", "neutral review"),
    Example("I would not watch this movie again but it was not a waste of time", "neutral review"),
    Example("this movie lacked any originality or depth", "neutral review"),
    Example("this movie was nothing special", "neutral review")]
    )

# print('The confidence levels of the labels are: {}'.format(response.labels))
print(response)
