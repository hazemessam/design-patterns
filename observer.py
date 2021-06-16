from time import sleep


class Observer:
    def __init__(self, subject, name):
        self.name = name
        self.subject: Subject = subject
        self.subject.attach(self)
        self.subjectState = self.subject.getState()


    def update(self):
        self.subjectState = self.subject.getState()
        print(f'{self.name} heard the change in the subject state ({self.subjectState})')


    def updateSubjectState(self, State):
        self.subject.setState(State)



class Subject:
    def __init__(self):
        self.state = None
        self.observers: list[Observer] = []
    
    
    def setState(self, state): 
        self.state = state
        self.notifyObservers()
    
    
    def getState(self): return self.state

    
    def attach(self, observer: Observer):
        self.observers.append(observer)


    def detach(self, observer: Observer):
        self.observers.remove(observer)


    def notifyObservers(self):
        for observer in self.observers:
            observer.update()



def main():
    subject = Subject()

    ob1 = Observer(subject, 'Ob1')
    ob2 = Observer(subject, 'Ob2')
    ob3 = Observer(subject, 'Ob3')


    print('ob1 changed the subject state')
    print('Wait 2s...')
    sleep(1)
    ob1.updateSubjectState('State1')

    print('ob2 changd the subject state')
    print('Wait 2s...')
    sleep(1)
    ob2.updateSubjectState('State2')


main()
