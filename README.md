# signLanguageTranslator

## Research Questions 
This research project aimed to explore three main questions in detail: 
*	Can incorporating emotion detection via facial expression recognition improve the performance of a sign language translation model? 
*	How are current systems impacted by not including the user’s emotion when translating sign language?
*	Does emotion influence every translation, or only specific types of sentences and phrases?

## Objectives
To answer these questions, I set about designing an experiment to explore the exact impact of incorporating facial expression into a machine learning model’s translation of British Sign Language. 

Firstly, a facial expression detector would be built to detect a subject’s face and return the user’s facial expression. 

Secondly, a model would be built to take in data corresponding to a user’s manual gesture only and translate this into text.

A series of phrases or sentences would be passed through this model, recording the results of each.

Thirdly, a model would be built that takes in both the user’s manual gesture data and the emotion data returned by the previous facial expression detector and translate these into text.

The same series of phrases and sentences would be passed through this new model, again with the results recorded for each.

An analysis would then be conducted on the results of this experiment, which was used to answer each of the research questions.

## Preprocessing Data
To preprocess the data needed to create these models, first the BOBSL daatset needs to be downloaded. After, run each of the following files, changing the file paths to be where the files have been stored on your system:
* extracting_facial_expressions
* extracting_keypoints
* extracting_subtitles

## Build Manual Model
To build the manual model, run the following file, again changing directory paths where needed, following commented instructions when necessary.
* Manual_Model

## Build Emotion Model
To build the manual model, run the following file, again changing directory paths where needed, following commented instructions when necessary.
* Emotion_Model

## Preprocessing Test Phrases
To preprocess the one hundred test phrases needed to test the models,  run each of the following files, changing the file paths to be where the files have been stored on your system:
* clipping_videos
* get_test_emotions
* get_test_keypoints
* get_test_subtitles

## Running Tests
To run the tests on these 100 phrases, run the following code for the Emotion Model and Manual Model respectively, changing the paths where needed:
* run_emotion_tests
* run_manual_tests

## Unused Files
Code was created to make a third model based on all features given in the BOBSL dataset. The model runs correctly, however the results provided did not provide any benefitial insight into the research project. This is because there was not enough time to fine tune the model into its most optimal form. The code has been provided in the unused folder, for reference. 
