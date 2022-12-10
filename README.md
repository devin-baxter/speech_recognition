# speech_recognition
Basic speech recognition app written in Python named "Freya"

Ensure that Google Text-to-Speech (gtts) is installed and up-to-date:

python -m pip install --upgrade gtts

python -m pip install --upgrade gtts-token

At this point in development FREYA can only understand a few commands. Run the program (python3 freya.py):
NOTE: If Freya did not hear you or could not understand the command you gave her, she will say "Sorry, I did not get that" and you should repeat the command.
Say "What is your name?" for Freya to tell you her name;
Say "What time is it?" for Freya to tell you the current time;
Say "Search" for Freya to ask, "What are we searching for?" and you will give her a topic to search. A web browser window will open to display a Google search results for the topic you asked Freya to search;
Say "Find location" for Freya to ask, "Which location are we looking up?" and you will give her a specific location, the more specific the better. A web browser window will open to display a Google Maps search of the location you gave to Freya.
*All of these commands except "What is your name?" require an active internet connection for Freya to find the relevant information.

This is the very beginning of an interactive speech application I hope to eventually link to machine learning trained in scientific research. The goal is to create a virtual scientific assisstant able to answer questions or look up data pertaining to real world journal articles for human researchers.
