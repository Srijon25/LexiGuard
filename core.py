import logging
from lexiguard.phrase_manager import PhraseManager
from lexiguard.voice_recognition import VoiceRecognizer
from lexiguard.utils import AlertSystem

class LexiGuard:
    def __init__(self, model_path: str, cancel_phrases_file: str):
        self.logger = logging.getLogger('LexiGuard')
        self.phrase_manager = PhraseManager(cancel_phrases_file)
        self.voice_recognizer = VoiceRecognizer(model_path)
        self.alert_system = AlertSystem()
        self.logger.info("LexiGuard initialized.")
    
    def start_monitoring(self):
        self.logger.info("Starting voice monitoring...")
        while True:
            audio = self.voice_recognizer.listen()
            if audio is None:
                continue
            transcript = self.voice_recognizer.transcribe(audio)
            if not transcript:
                continue
            self.logger.debug(f"Transcript: {transcript}")
            detected_phrases = self.phrase_manager.detect_phrases(transcript)
            if detected_phrases:
                self.logger.info(f"Detected cancel phrases: {detected_phrases}")
                confidence = self.voice_recognizer.get_confidence(transcript, detected_phrases)
                if confidence > 0.8:
                    self.alert_system.trigger_alert(detected_phrases, confidence)
                else:
                    self.logger.info(f"Low confidence ({confidence}), suggesting alternatives.")
                    alternatives = self.phrase_manager.suggest_alternatives(detected_phrases)
                    self.alert_system.suggest_alternatives(alternatives)
            else:
                self.logger.debug("No cancel phrase detected.")
