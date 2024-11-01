from functions import fasterRandom

def random_method(boxes, chances):
    prisoners = len(boxes)
    results = []

    for prisoner in range(prisoners):    
        prisoner = prisoner + 1
        closed_boxes = boxes.copy()

        success = False
        boxes_opened = 0

        for chance in range(chances):
            boxes_opened += 1
            
            choice_index = fasterRandom(prisoners)
            choice = closed_boxes[choice_index]
            
            if choice == prisoner:
                success = True
                break
            else:
                del closed_boxes[choice_index]  
            
        results.append([prisoner, success, boxes_opened])

    return results

def loop_method(boxes, chances):
    prisoners = len(boxes)
    results = []
    
    for prisoner in range(prisoners):    
        prisoner = prisoner + 1

        success = False
        previous_choice = prisoner
        boxes_opened = 0

        for _ in range(chances):
            boxes_opened += 1
            
            choice = boxes[previous_choice - 1]

            if choice == prisoner:
                success = True
                break
            else:
                previous_choice = choice
        
        results.append([prisoner, success, boxes_opened])

    return results

strategy_list = [random_method, loop_method]
