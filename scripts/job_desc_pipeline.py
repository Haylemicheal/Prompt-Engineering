from scripts.dataloader import DataLoader
from scripts.generate import Generate

class Job_Pipeline:
    def __init__(self):
        self.dl = DataLoader()
        self.gen = Generate()

    def make_train_prompt(self, data):
        """Make a prompt for news classifier
        Args:
            data: jobs data
        Returns:
            prompt: prepared prompt
        """
        doc1 = data[0]['document']
        tokens = data[0]['tokens'][0]
        train = ""
        train = "document: {}\nExtracted:\n".format(doc1)
        train = train + "text: {},start: {},end: {},token_start: {},token_end: {},entityLabel: {}\n".format(tokens['text'], tokens['start'], tokens['end'],tokens['token_start'],tokens['token_end'],tokens['entityLabel'])
        tokens = data[0]['tokens'][1]
        train = train + "text: {},start: {},end: {},token_start: {},token_end: {},entityLabel: {}\n".format(tokens['text'], tokens['start'], tokens['end'],tokens['token_start'],tokens['token_end'],tokens['entityLabel'])
        tokens = data[0]['tokens'][2]
        train = train + "text: {},start: {},end: {},token_start: {},token_end: {},entityLabel: {}\n".format(tokens['text'], tokens['start'], tokens['end'],tokens['token_start'],tokens['token_end'],tokens['entityLabel'])
        tokens = data[0]['tokens'][3]
        train = train + "text: {},start: {},end: {},token_start: {},token_end: {},entityLabel: {}\n".format(tokens['text'], tokens['start'], tokens['end'],tokens['token_start'],tokens['token_end'],tokens['entityLabel'])
        train = train + '---\n'
        return train

    def pipeline(self, test_doc):
        """Pipeline for job description entity gen"""
        data = self.dl.read_json('../data/relations_dev.txt')
        train = self.make_train_prompt(data)
        test_doc = "document: " + test_doc + "\nExtracted:\n"
        prompt = train + test_doc
        self.gen.generate(prompt)
        return self.gen.get_pred()
