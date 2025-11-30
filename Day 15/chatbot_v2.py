# This file contains implementation of a python chatbot created using OOP approach.

from datetime import datetime


class Chatbot():
    def __init__(self, name : str ="Nina") -> None:
        self.name : str = name
        self.__memory : list[str] = list()
    
    @staticmethod
    def __contains(*keywords : str, text : str | list[str]) -> bool:
        for word in keywords:
            if " " in word:
                break
        else:
            text = text.split(" ") if isinstance(text, str) else text
        
        for word in keywords:
            if word in text:
                return True
        else:
            return False
    
    def __remember(self, prompt : str) -> None:
        self.__memory.append(prompt)
        
        if len(self.__memory) > 3:
            self.__memory.pop(0)
        
        return None
    
    def __response(self, prompt : str) -> str:
        prompt = prompt.lower()
        
        # Follow up responses (that use bot memory)
        if self.__contains("how are you", "and you", "how about you", text=prompt) and self.__contains("hello", "hi", text=" ".join(self.__memory)):
            return "I am fine, happy to meet you. Let me know if you need any help."
        elif self.__contains("tomorrow", text=prompt) and self.__contains("weather", text=" ".join(self.__memory)):
            return "Tomorrow there is a 50% chance of rain, with an average temprature of 16 degrees celcius"
        elif self.__contains("what", "how", text=prompt) and self.__contains("listen", "let me tell you", text=" ".join(self.__memory)):
            return "I don't know, what do you think about that."
        elif self.__contains("sad", "depressed", "concern", text=prompt) and self.__contains("don't know", "?", text=self.__memory[-1]):
            return "Don't worry so much, everything will be fine afterall, just do what you're supposed to do."
        
        # General responses
        if self.__contains("hi", "hello", text=prompt):
            return f"Hello! I am {self.name}. How are you?"
        elif self.__contains("how are you", "is it going", text=prompt):
            return "I am Good, and you?"
        elif self.__contains("what time is it", "current time", text=prompt):
            return f"The current time is: {datetime.now().strftime("%H:%M:%S")}"
        elif self.__contains("weather", "temprature", text=prompt):
            return "The weather today will be cloudy and cold with an average temprature of 18 degrees celcius."
        elif self.__contains("listen", "let me tell you", text=prompt):
            return "Go ahead..."
        elif self.__contains("don't know", "confused", text=prompt):
            return "And, what else do you feel?"
        elif self.__contains("thank you", "thanks", text=prompt):
            return "I am happy to help you."
        elif self.__contains("goodbye", "bye", text=prompt):
            return "Bye! Have a nice day."
        elif self.__contains("help", "commands", text=prompt):
            return "I can only understand: Help/Commands, Hi/Hello, What time is it/Current time, Weather/Temprature, Thank You/Thanks, Goodbye/Bye, and a few follow up questions."
        
        return "Sorry, I cannot answer that question right now."
    
    def start(self) -> None:
        print(f"Bot ({self.name}) is starting. Type \"Help\" for commands or \"Bye\" to quit conversation.")
        
        while True:
            user_prompt : str = input("\nYou: ").strip()
            bot_response : str = self.__response(user_prompt)
            
            print(f"{self.name}: {bot_response}")

            if self.__contains("goodbye", "bye", text=user_prompt.lower()):
                break
            
            self.__remember(user_prompt)
    

def main() -> None:
    bot : Chatbot = Chatbot()
    bot.start()


if __name__ == "__main__":
    main()
    
# The code quality is not very good, it lacks annotation, docstrings, and have a few logical errors.