import cohere
from cohere.classify import Example
import os
from dotenv import load_dotenv
load_dotenv()

class Generate:
    def __init__(self):
        self.pred = ""
        self.response = ""

    def generate(self, prompt):
        """A method to generate an entity"""
        co = cohere.Client("gXCLbW64PfL9gOzVPgpYPgFZ8wBFcXJ3yYZj7YqT")
        self.response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=50,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["---"],
        return_likelihoods='NONE')

    def get_pred(self):
        """Get predection"""
        return self.response.generations[0].text