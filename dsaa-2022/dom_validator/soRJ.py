import re

def is_validate_dom(dom_text : str) -> bool:

    """ dom 문서인 str 타입의 데이터를 받은 후 해당 데이터가 올바른 dom 문서인지 아닌지 확인 하는 코드 
        반드시 stack 또는 queue 를 사용하여 구현할 것
    Args:
        dom_text (str) : dom 문서

    Returns:
        is_valudate_dom (bool) : 해당 문서가 올바른 dom인지 확인하는 코드
    
    """
    
    check = '/'

    stack = []
    queue = []
    output = ''
    
    dom_text = dom_text.replace("<","(")
    dom_text = dom_text.replace(">",")")
    dom_text = re.findall('\(([^)]+)', dom_text)
    for i in range(len(dom_text)):
        print(dom_text[i])
        dom_text[i] = dom_text[i].split(" ")[0]
    print(dom_text)
    
    for s in dom_text:
        if '/' not in s:
            stack.append(s)

    for s in dom_text:
        if '/' in s:
            queue.append(s)
    

            
    for i in range(len(queue)):
        queue[i] = queue[i].lstrip('/')


    for i in range(len(queue)):
        if stack.pop() == queue.pop(0):
            print('pass')
        else:
            return False


    if stack == [] and queue == []:
        return True
    


example ="""<data>
            <items>
                <item name="item1">item1abc</item>
                <item name="item2">item2abc</item>
            </items>
        </data>
        """.strip()
print(is_validate_dom(example))
# True



# output_list = []
# pregress_stack= []

# def is_validate_dom(dom_text : str) -> bool:

#     """ dom 문서인 str 타입의 데이터를 받은 후 해당 데이터가 올바른 dom 문서인지 아닌지 확인 하는 코드 
#         반드시 stack 또는 queue 를 사용하여 구현할 것
#     Args:
#         dom_text (str) : dom 문서

#     Returns:
#         is_valudate_dom (bool) : 해당 문서가 올바른 dom인지 확인하는 코드
    
#     """
#     OPERATOR = set({'<', '>', '/'})
#     PRIORITY = {'<':1, '>': 2, '/':3}
    
#     stack = []
#     queue = []
#     output = ''
    
#     for ch in dom_text:
#         if ch not in "<":
#             output += ch
            
#             if ch == ">":
                
#                 output = output.lstrip().rstrip('>')
#                 output = output.split()[0]
#                 print(output)
#                 stack.append(output)
                
#                 output = ''
#                 continue
#             else:
#                 False

#     # queue = [s for s in stack if '/' in s]
#     for s in stack:
#         if '/' in s:
            
#             queue.insert(0, s)
            
#     for i in range(len(queue)):
#         if queue[i] in stack:
            
#             stack.remove(queue[i])
#             queue[i] = queue[i].lstrip('/')

    
#     # for i in range(len(stack)):
#     #     if stack[i] in OPERATOR:
            
#     last = queue.pop(0)
#     queue.append(last)
    
#     for i in range(len(queue)):
#         if stack.pop() == queue.pop(0):
#             print('pass')
#         else:
#             return False

#     if stack == [] and queue == []:
#         return True
    
    




#     # for ch in dom_text:
#     #     if ch not in OPERATORS:
            


#     # for ch in dom_text:
#     #     if ch not in OPERATORS:
#     #         output += ch
#     #     elif ch == '<':
#     #         stack.append('<')
#     #     elif ch == '>':
#     #         while stack and stack[-1] != '<':
#     #             output += stack.pop()
#     #         stack.pop()
#     #     else:
#     #         while stack and stack[-1] != '<' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
#     #             output += stack.pop()
#     #         stack.append(ch)
#     # while stack:
#     #     output += stack.pop()

#     # return output


# print(is_validate_dom("<1 dkfjfdf> <2> </2> <dkfj kdlfjk> </dkfj> <4> </4> </1 dfdfjbv>"))