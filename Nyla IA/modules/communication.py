class Communicator:
    def contact_candidates(self, processed_data):
        # Simulate sending emails or messages
        print("Contacting candidates...")
        responses = []
        for candidate in processed_data:
            response = self._send_email(candidate)
            responses.append(response)
        return responses

    def _send_email(self, candidate):
        # Simulate email sending
        print(f"Sending email to {candidate['name']} at {candidate['email']}...")
        return {"candidate": candidate["name"], "response": "interested"}