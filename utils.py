import logging

class AlertSystem:
    def __init__(self):
        self.logger = logging.getLogger('AlertSystem')
    
    def trigger_alert(self, phrases, confidence):
        self.logger.info(f"Alert: Cancel phrase(s) {phrases} detected with confidence {confidence}.")
        print(f"*** ALERT: Cancel phrase(s) detected: {phrases} (confidence: {confidence:.2f}) ***")
    
    def suggest_alternatives(self, suggestions):
        print("Suggested alternative phrases based on detected input:")
        for phrase, alternatives in suggestions.items():
            print(f"  {phrase}: {alternatives if alternatives else 'No close matches found'}")
