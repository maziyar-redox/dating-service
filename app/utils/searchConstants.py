from core.ConstantObjects import placesQuestionList, foodsQuestionList

def SearchPlacesAndFoodsArray(phase_one: int, phase_two: int) -> bool:
    phase_one_status = False
    getPhaseOneData = placesQuestionList[0].question_list
    for val in getPhaseOneData:
        if val.id == phase_one:
            phase_one_status = True
            break
    if phase_one_status == False:
        return False
    phase_two_status = False
    getPhaseTwoData = foodsQuestionList[0].question_list
    for val in getPhaseTwoData:
        if val.id == phase_two:
            phase_two_status = True
            break
    if phase_two_status == False:
        return False
    return True