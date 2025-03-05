class Chatbot:
    def __init__(self, api):
        self.api = api

    def get_response(self, user_input):
        response = self.api.call_llama_api(user_input)
        return response