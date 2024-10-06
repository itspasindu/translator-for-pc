#Requirements:
Language Detection: Automatically detect the language of the input text.
Language Translation: Allow the user to select the target language for translation.

#Text Areas: One for input and another for translated output.
Drop-down Menus: For selecting the source and target languages.
Translation Functionality: Translate the text using a Python library such as googletrans or deep_translator.

#Step-by-Step Implementation:
Install Required Libraries: You’ll need the googletrans or deep_translator package for translation:

pip install googletrans==4.0.0-rc1

#Explanation:
Language Detection: When the source language is set to "Auto Detect," the app detects the language using translator.detect.
Translation: The translate function translates the input text based on the selected languages.

#GUI:
A Text widget is used for input and output text areas.
Combobox widgets let users select source and target languages.
A button triggers the translation when clicked.

#Customization:
You can extend the list of available languages by modifying the languages list.
Improve the user interface based on your design by adding colors, fonts, or other GUI elements.
