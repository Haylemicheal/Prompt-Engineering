
## Overview
A client has a system that collects news artifacts from web pages, tweets, facebook
posts, etc. The client is interested in scoring a given new artifact against a topic. The
client has hired experts to score a few of these news items in the range from 0 to 10;
a score of 0 means the news item is totally NOT relevant while a score of 10 means
the news item is very relevant. The range of results between 0 and 10 signifies the
degree of relevance of the news item to the topic.

The client wants to explore how useful existing LLMs such as GPT-3 are for this task.
Our task is to explore the efficiency of GPT3-like LLMs to this task. If the
recommendation is positive, We must demonstrate that our strategies to design
prompts are reproducible and produce a consistent result.

We should also set up an MLOps pipeline that helps automate the task of using
different LLMs and different topics. Our pipeline should also allow future
improvements in the prompt design to be integrated without breaking the system. A
centralized log system should be incorporated into your pipeline to help monitor
outputs, cost, performance, and other relevant artifacts



## Objectives
- Understand the algorithms and techniques that goes into building large language models 
- Design a pipeline that takes a news item (e.g. title +  description + body) or a job description and returns a score for the news item and list of entities (and potentially their relationship) for the job description  according to stored examples. Consider the following while designing your pipeline
    * Think about in what format you want to receive the news item to be processed
    * Think about how to select the best samples for the given news item
    * Think about how to pre-process the incoming item as well as the pre-defined samples
    * Think about how to compose a prompt that gives the best result for the given item
    * Think about the post-processing step you need to do to increase the accuracy as well as return in the format required
- Write a flask or fastapi backend. The API should have at least two endpoints 
    * /bnewscore - for scoring  breaking news that may lead to public unrest
    * /jdentities - for extracting entities from job description

##  Dataset
Data 1
- The data for this challenge can be found [here](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit?usp=sharing&ouid=108085860825615283789&rtpof=true&sd=true).
Data 2
- [For development and training](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt).
- [For testing and final reporting](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt).
## Project Structure
- data: Contains the dataset
- scripts: Contains script codes
- logs: contains log files
- tests: Unit test files
- .github/workflows- Contains yml configration file of github acyion
- .dvc: Data versioning related configration and files
- .travis.yml: Contains config file for travis ci/cd 

## Author

- [Haylemicheal Berihun](https://www.linkedin.com/in/haylemicheal-berihun-a20320aa)
- 10academy team

