import re

def is_validate_dom(dom_text : str) -> bool:

    """ dom 문서인 str 타입의 데이터를 받은 후 해당 데이터가 올바른 dom 문서인지 아닌지 확인 하는 코드 
        반드시 stack 또는 queue 를 사용하여 구현할 것
    Args:
        dom_text (str) : dom 문서

    Returns:
        is_valudate_dom (bool) : 해당 문서가 올바른 dom인지 확인하는 코드
    
    """
    
    stack = []
    queue = []
        
    # 1개 이상의 태그를 포함하는 경우만 진행
    if '<' and '>' in dom_text:
        dom_text = dom_text
        if '<>' in dom_text:
            return False
        elif dom_text[-1] != '>':
            return False
        elif dom_text[0] != '<':
            return False
        else:
            dom_text = dom_text
    else:
        return False
    
    
    dom_text = dom_text.replace("<","(")
    dom_text = dom_text.replace(">",")")    # re를 쓰기위한 과정
    dom_text = dom_text.replace("  ", " ")  # 나중에 공백으로 자르기 위해 공백을 한 칸으로 줄여줌
    dom_text = re.findall('\(([^)]+)', dom_text) # ()사이의 문자들만 추출하여 리스트로 저장

    for i in range(len(dom_text)):
        dom_text[i] = dom_text[i].split(" ")[0] # 속성 정보를 제외하고 태그로만 비교하게 만듦

    for i in range(len(dom_text)):
        if '/' not in dom_text[i]:
            stack.append(dom_text[i])   # 태그의 부모들을 stack에 넣어줌
        elif '/' in dom_text[i]:
            dom_text[i] = dom_text[i].lstrip('/')   # 태그의 자식들을 '/'를 지워주고
            queue.append(dom_text[i]) # queue에 넣어줌
            
    print('Stack : ',stack)
    print('Queue : ',queue)
    
    for i in range(len(stack)):
        if stack[0] == queue[-1]:
            stack.pop(0)
            queue.pop()
            

    if stack == [] and queue == []:     # stack과 queue 모두 빈 리스트일때 True를 반환 아닐경우 False
        return True
    else:
        return False
    

    
    
example ="""<data>
            <items>
                <item name="item1">item1abc</item>
                
                <item name="item2">item2abc</item>
            </items>
        </data>
        """.strip()
print(is_validate_dom(example))
# True

example2 ="""<items>
             <data>
                 <items name="item1">item1abc</items>
                 
                 <item name="item2">item2abc</item>
             </items>
         </data>
         """.strip()
print(is_validate_dom(example2))
# False

example3 = "<a>ddd</a>"
print(is_validate_dom(example3))
# True

example4 = "<></>"
print(is_validate_dom(example4))
# False