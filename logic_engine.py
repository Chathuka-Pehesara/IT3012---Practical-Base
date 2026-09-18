class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def tell_fact(self, fact_string: str):
        """Add a unique string fact to the Knowledge Base."""
        self.facts.add(fact_string)

    def tell_rule(self, premise_list: list, conclusion_string: str):
        """Add a rule as a Tuple of (premises, conclusion)."""
        self.rules.append((premise_list, conclusion_string))

    def clear_facts(self):
        """Empty the facts set."""
        self.facts.clear()

    def forward_chain(self):
        """Deduce new facts using data-driven forward chaining."""
        new_facts_added = True
        
        while new_facts_added:
            new_facts_added = False
            
            for premises, conclusion in self.rules:
                if conclusion not in self.facts:
                    # Modus Ponens Check
                    if all(premise in self.facts for premise in premises):
                        self.facts.add(conclusion)
                        new_facts_added = True
