
'''
from transformers import pipeline
model_name = "google/pegasus-xsum"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
article="My name is Bob and I like play football"

summ = summarizer(article,max_length=9,min_length=1)
print(summ[0]["summary_text"])
'''









from transformers import pipeline
from nltk.tokenize import word_tokenize
model_name = "google/pegasus-xsum"
#model_name="facebook/bart-large-cnn"
summarizer = pipeline("summarization", model_name )

article = """Lucas goes to school every day of the week. He has many subjects to go to each school day: English, art, science, mathematics, gym, and history. His mother packs a big backpack full of books and lunch for Lucas.
His first class is English, and he likes that teacher very much. His English teacher says that he is a good pupil, which Lucas knows means that she thinks he is a good student.
His next class is art. He draws on paper with crayons and pencils and sometimes uses a ruler. Lucas likes art. It is his favorite class.
His third class is science. This class is very hard for Lucas to figure out, but he gets to work with his classmates a lot, which he likes to do. His friend, Kyle, works with Lucas in science class, and they have fun.
Then Lucas gets his break for lunch. He sits with Kyle while he eats. The principal, or the headmaster as some call him, likes to walk around and talk to students during lunch to check that they are all behaving.
The next class is mathematics, which most of the students just call math. Kyle has trouble getting a good grade in mathematics, but the teacher is very nice and helpful.
His fourth class is gym. It is just exercising.
History is his last class of the day. Lucas has a hard time staying awake. Many lessons are boring, and he is very tired after doing gym."""
wordCount=len(word_tokenize(article))
size=10
min=5
max=7
maxLen=round((wordCount/size)*max)
minLen=round((wordCount/size)*min)
print(wordCount,minLen,maxLen)
summary = summarizer(article, min_length=minLen, max_length=maxLen)
print(summary[0]["summary_text"])


'''
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as tf_text


text_generator = hub.load(
    '/home/tullio/PROJECTS/dsml/dsml/dalleapp/models/textsummary/bbc')
input_sents = tf.constant(['Lucas goes to school every day of the week.'])
output_summaries = text_generator.signatures["default"](input_sents)
print(output_summaries)
'''