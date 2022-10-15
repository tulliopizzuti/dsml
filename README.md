# DALLE APP
This project contains a web application that combines, Text Summarization, 
Word Tree visualization technique and the generation of images with DALLE 2.

### Installation

For installation, if you have installed anaconda on your device, you can run the setup file ([Win](https://github.com/tulliopizzuti/dsml/blob/main/dsml/setup.bat),
[Lin](https://github.com/tulliopizzuti/dsml/blob/main/dsml/setup.sh)) to install all the necessary packages.
Otherwise you can use pip to install the packages as follows:

      pip install django
      pip install djangorestframework
      pip install nltk
      pip install tranformers
      pip install dalle2



### Page Settings

The project presents as the initial page of the application a 'Settings' section in which there are the texts, 
on which we can make changes, deletions or add others. At the bottom of the page is the form where you can change 
the API key for generating images with the Dalle2 model, the number of images you want to generate and the model 
with which to summarize the texts.

![alt text](https://github.com/tulliopizzuti/dsml/blob/main/readme_file/settings.png)

### Page Texts

In the texts page there is a drop-down menu where you can choose between various saved texts, which can be highlighted to make the summary. 
Through the WordTree button in the tooltip it is possible to send the text to the appropriate page for processing.

![alt text](https://github.com/tulliopizzuti/dsml/blob/main/readme_file/texts.png)

### Page WordTree

On this page it is possible to summarize the text entered in the form. 
Subsequently, through the WordTree visualization technique, it is possible to select a sentence from the text on which to generate images.

![alt text](https://github.com/tulliopizzuti/dsml/blob/main/readme_file/wordtree.png)

### Page Dalle

Once the phrase has been selected from the WordTree and generated the images through the appropriate button, the images are shown at the bottom of the page.

![alt text](https://github.com/tulliopizzuti/dsml/blob/main/readme_file/dalle.png)

### Demo Dalle App

https://user-images.githubusercontent.com/32485751/196000818-a0743cd7-0072-48d9-8baa-fba1825f7c0e.mp4



