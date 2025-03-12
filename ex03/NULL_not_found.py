def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : {} {}".format(object, type(object)))
    elif isinstance(object, float) and object!=object:
        print("Cheese: {} {}".format(object, type(object)))
    elif object == 0 and type(object) == int:
        print("Zero : {} {}".format(object, type(object)))
    elif object =="":
        print("Empty : {} {}".format(object, type(object)))
    elif object is False:
        print("Fake: {} {}".format(object, type(object)))
    else:
        print("Type not Found")
        return 1
    return 0


