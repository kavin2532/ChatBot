from tkinter import Tk, Text, Button, END, Scrollbar, VERTICAL, RIGHT, Y
from chatbot import Chatbot
from llama_api import LlamaAPI

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot Tool")

        self.message_box = Text(master, height=10, width=50)
        self.message_box.pack()

        self.submit_button = Button(master, text="Submit", command=self.get_response)
        self.submit_button.pack()

        self.response_box = Text(master, height=10, width=50)
        self.response_box.pack()

        self.scrollbar = Scrollbar(master, command=self.response_box.yview, orient=VERTICAL)
        self.response_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Create an instance of the LlamaAPI
        api_instance = LlamaAPI()

        # Pass the api_instance to the Chatbot constructor
        self.chatbot = Chatbot(api_instance)

    def get_response(self):
        user_input = self.message_box.get("1.0", END).strip()
        if user_input:
            response = self.chatbot.get_response(user_input)
            self.response_box.delete("1.0", END)
            self.response_box.insert(END, response)
            self.message_box.delete("1.0", END)

if __name__ == "__main__":
    root = Tk()
    app = ChatbotApp(root)
    root.mainloop()