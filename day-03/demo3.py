def can_vote(age):

    """
    this function is made to check if a person is eligible for voting
    :param age: age of a person
    :return: nothing

    """
    if(age>=18):
        print("person can vote")
    else:
        print("person cannot vote")

age=17
can_vote(age) 

age2=22
can_vote(age2)