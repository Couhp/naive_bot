
##
#   My Naive Bot Class
#   author@ Couhp
##
class MyBot :

    def __init__(self, name="bot"):
        self.__bot_name = name
        self.__user = {"name":"", "location":""}
        return
    
    def __preprocessing (self, input_str="") :
        return input_str.replace("  "," ").split(".")


    def __greeting_detector (self, input_str="") :
        greeting_data = ["chào", "xin chào"]
        introduce_data = ["tên tôi là", "tôi là"]
        if any (x in input_str for x in greeting_data) or any (x in input_str for x in introduce_data):
            return 1    # This is confidence of detector result 
        else :
            return 0
    
    def __greeting_response (self, input_str="") :
        greeting_data = ["chào", "xin chào"]
        introduce_data = ["tên tôi là", "tôi là"]
        if any (x in input_str for x in greeting_data) :
            return "Chào. Tên bạn là gì ?"
        if any (x in input_str for x in introduce_data) :
            name = [word for word in input_str.split() if str.istitle(word[0])]
            self.__user["name"] = ' '.join(name)
            return "xin chào " + self.__user["name"] +\
             ".\nTên tôi là " + self.__bot_name + ".\nTôi giúp gì được bạn"


    def __weather_detector (self, input_str="") :
        weather_data = ["thời tiết", "trời", "thế nào"]
        counter = 0
        for word in weather_data :
            if word in input_str : 
                counter += len(word.split())
        return counter / len(input_str.split()) 
        # Confidence is number of word about weather question in data 

    def __weather_response (self, input_str="") :
        location = [word for word in input_str.split() if str.istitle(word[0])]
        self.__user["location"] = ' '.join(location)
        return self.__user["location"] + " hôm nay trời đẹp nhé.\n" + \
               self.__user["name"] +  " đi chơi với bạn gái đi."

    
    def get_response (self, input_str) :
        sentences = self.__preprocessing(input_str)
        response = ""
        for sentence in sentences :
            cf1 = self.__greeting_detector(input_str=sentence)
            cf2 = self.__weather_detector(input_str=sentence)
            if cf1 > cf2 :
                response += self.__greeting_response(input_str=sentence)
            else :
                response += self.__weather_response(input_str=sentence)
        return response
