import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocess:
    def get_X_y(self, df, features, target):
        """Get the features from the dataframe
        Args:
            df: dataframe
            features: Feature cols
        Returns:
            df[features]: dataframe containing features
        """
        X = df[features]
        y = df[target]
        return X,y

    def data_split(self, X, y):
        """Train test splitting
        Args:
            X: Features
            y: Target
        Returns:
            train, test, labels_train, labels_test
        """
        train, test, labels_train, labels_test = train_test_split(
            X,y, test_size=0.25, random_state=0)
        return train, test, labels_train, labels_test

    def change_to_category(self, df, name, c1, c2):
        """Change values to categorical
        Args:
            name: name of the column
            df: dataframe
            c1: category 1
            c2: category 2
        Returns:
            df: changed data
        """
        df[name] = df[name].apply(lambda x: c1 if x<1 else c2)
        return df
    
    def merging_cols(self, train, labels_train):
        """Merging columns
        Args:
            train: train data
            labels_train: labels
        Returns:
            train: merged data
        """
        train['merged'] = 'Title: ' + train['Title'] +'\n'+ 'Description: '+train['Description']+'\n'+'Analyst_Average_Score: '+labels_train +'\n---\n'
        return train

    def test_data_prepare(self, title, desc):
        """Prepare the test for prompt
        Args:
            test: test dataframe
            i: index
        Returns:
            test_: test prepared data
        """
        test_ = 'Title: ' + title +'\n'+ 'Description: '+desc+'\n' +'Analyst_Average_Score: '
        return test_

    def get_prompt(self, train, test):
        """Get the prompt text
        Args:
            train: Train df
            test: test prompt
        Returns:
            prompt: The prompt
        """
        prompt = ""
        for i in train['merged']:
            prompt+=i
        prompt += prompt + test
        return prompt


    
