

########

def whoDoYouknow() :
    people = input ('People you know separated by comas: ')
    peopleList = people.split(',')
    return peopleList

def askUser():
    people = whoDoYouknow()
    person = input('Enter the name of someone you know')
    if person in people:
        print('You know {}'.format(person))

askUser()