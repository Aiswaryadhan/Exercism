def commands(binary_str):
    action_mapping = {
        1: "wink",
        2: "double blink",
        3: "close your eyes",
        4: "jump"
    }
    final_result = []
    count = 1
    while len(binary_str)>0:
        char = int(binary_str[-1])
        binary_str = binary_str[:-1]
        if char:
            if count == 5:
                return final_result[::-1]
            else:
                final_result.append(action_mapping[count])
        count+=1
    return final_result
            
