from collections import deque


def stock_availability(flavors, action, *optional):
    flavors = deque(flavors)

    if action == 'delivery':

        for flavor in optional:
            flavors.append(flavor)

    elif action == 'sell':
        if optional:
            if str(optional[0]).isdigit():
                boxes_to_remove = int(optional[0])
                if len(flavors) > boxes_to_remove:
                    for i in range(boxes_to_remove):
                        flavors.popleft()
                else:
                    flavors.clear()
            else:
                for order in optional:
                    if order in flavors:
                        while order in flavors:
                            flavors.remove(order)
        else:
            if flavors:
                flavors.popleft()

    return list(flavors)


print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "pal",'rock','vanilla'))








