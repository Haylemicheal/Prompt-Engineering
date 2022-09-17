from scripts.dataloader import DataLoader
from scripts.preprocess import Preprocess
from scripts.generate import Generate

class Pipeline:
    def __init__(self):
        self.dl = DataLoader()
        self.process = Preprocess()
        self.gen = Generate()

    def pipeline(self, title, desc):
        df = self.dl.read_xls('../data/Example_data.xlsx')
        df = self.process.change_to_category(df, 'Analyst_Average_Score', 'low', 'high')
        X, y = self.process.get_X_y(df, ['Title','Description','Body'], 'Analyst_Average_Score')
        train, test, labels_train, labels_test = self.process.data_split(X, y)
        train = self.process.merging_cols(train, labels_train)
        test_ = self.process.test_data_prepare(title, desc)
        prompt = self.process.get_prompt(train, test_)
        self.gen.generate(prompt)
        return self.gen.get_pred()


