import re

class RuleEngine:
    def __init__(self, rules):
        self.rules = rules  # Load from JSON or DB

    def scan(self, code):
        results = []
        for rule in self.rules:
            matches = re.finditer(rule['pattern'], code)
            for match in matches:
                results.append({
                    "line": code[:match.start()].count('\n') + 1,
                    "pattern": rule['pattern'],
                    "message": rule['description'],
                    "severity": rule['severity']
                })
        return results
