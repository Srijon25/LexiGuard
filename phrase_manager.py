import json
import difflib
import logging

class PhraseManager:
    def __init__(self, phrases_file: str):
        self.logger = logging.getLogger('PhraseManager')
        self.phrases_file = phrases_file
        self.load_phrases()
    
    def load_phrases(self):
        try:
            with open(self.phrases_file, 'r') as f:
                self.phrases = json.load(f)
            self.logger.info(f"Loaded {len(self.phrases)} cancel phrases.")
        except Exception as e:
            self.logger.error(f"Failed to load phrases: {e}")
            self.phrases = []
    
    def detect_phrases(self, text: str):
        detected = []
        for phrase in self.phrases:
            if phrase in text:
                detected.append(phrase)
        return detected
    
    def suggest_alternatives(self, detected_phrases):
        suggestions = {}
        for phrase in detected_phrases:
            close_matches = difflib.get_close_matches(phrase, self.phrases, n=3)
            suggestions[phrase] = close_matches
        return suggestions
    
    def add_phrase(self, phrase: str):
        if phrase not in self.phrases:
            self.phrases.append(phrase)
            self.save_phrases()
            self.logger.info(f"Added new cancel phrase: {phrase}")
    
    def remove_phrase(self, phrase: str):
        if phrase in self.phrases:
            self.phrases.remove(phrase)
            self.save_phrases()
            self.logger.info(f"Removed cancel phrase: {phrase}")
    
    def save_phrases(self):
        try:
            with open(self.phrases_file, 'w') as f:
                json.dump(self.phrases, f, indent=2)
            self.logger.info("Saved cancel phrases to file.")
        except Exception as e:
            self.logger.error(f"Failed to save phrases: {e}")
