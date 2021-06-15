from enum import Enum, auto


class RequestType(Enum):
    CONFERENCE = auto()
    PURCHASE = auto()



class Request:
    def __init__(self, requestType: RequestType, amount: float):
        self.requestType = requestType
        self.amount = amount



class Handler:
    def __init__(self):
        self.successor: Handler = None


    def setSuccessor(self, successor):
        self.successor = successor


    def handleRequest(self, request: Request): pass



class Director(Handler):
    def handleRequest(self, request: Request):
        if request.requestType == RequestType.CONFERENCE:
            print('The director accepted the request.')
        else:
            self.successor.handleRequest(request)



class VP(Handler):
    def handleRequest(self, request: Request):
        if request.requestType == RequestType.PURCHASE and request.amount <= 2500:
            print('The VP accepted the request.')
        else:
            self.successor.handleRequest(request)



class CEO(Handler):
    def handleRequest(self, request: Request):
        print('The CEO accepted the request.')



def Main():
    seif = Director()
    omer = VP()
    hazem = CEO()

    seif.setSuccessor(omer)
    omer.setSuccessor(hazem)

    req = Request(requestType=RequestType.CONFERENCE, amount=1000)
    seif.handleRequest(request=req)
    
    req = Request(requestType=RequestType.PURCHASE, amount=2500)
    seif.handleRequest(request=req)
    
    req = Request(requestType=RequestType.PURCHASE, amount=3000)
    seif.handleRequest(request=req)


Main()
