class TalentSelector:
    def preselect_candidates(self, responses):
        # Simulate preselection based on responses
        print("Preselecting candidates...")
        selected_candidates = [response["candidate"] for response in responses if response["response"] == "interested"]
        return selected_candidates