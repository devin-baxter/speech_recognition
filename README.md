# speech_recognition
Basic speech recognition app written in Python named "Freya"

Ensure that all dependencies are installed and up-to-date:  
  
pip install --upgrade SpeechRecognition  

pip install --upgrade playsound  

pip install --upgrade pyaudio  

pip install --upgrade gtts  

pip install --upgrade gtts-token

At this point in development FREYA can only understand a few commands. Run the program from the terminal with the command:  
  
python3 freya.py  

Say "What is your name?" for Freya to tell you her name;  
  
Say "What time is it?" for Freya to tell you the current time;  
  
Say "Search" for Freya to ask, "What are we searching for?" and you will give her a topic to search. A web browser window will open to display Google search results for the topic you asked Freya to search;  
  
Say "Find location" for Freya to ask, "Which location are we looking up?" and you will give her a specific location, the more specific the better. A web browser window will open to display a Google Maps search of the location you gave to Freya.  

To end the program, say "Freya, go to sleep" or press Ctrl+Z in the terminal.  

NOTE: If Freya did not hear you or could not understand the command you gave her, she will say "Sorry, I did not get that" and you should repeat the command. The program can stall and require a restart if Freya does not hear or recognize a command for 10 seconds.  
*All of these commands except "What is your name?" require an active internet connection for Freya to find the relevant information.  
  
This is the very beginning of an interactive speech application I hope to eventually link to machine learning trained in scientific research. The goal is to create a virtual scientific assisstant able to answer questions or look up data pertaining to real world journal articles for human researchers.  
