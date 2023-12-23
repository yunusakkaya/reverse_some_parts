'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
    def reverse_words(segment):
        
        return ' '.join(word[::-1] for word in segment.split())

    result = []
    temp = ''
    in_parentheses = False
    for char in mystr:
        if char == '(':
            if in_parentheses:
                temp += char
            else:
                result.append(reverse_words(temp))
                temp = char
            in_parentheses = True
        elif char == ')':
            in_parentheses = False
            temp += char
            result.append(temp[1:-1])  
            temp = ''
        elif char == ' ':
            if in_parentheses:
                temp += char
            else:
                result.append(reverse_words(temp))
                result.append(char)
                temp = ''
        else:
            temp += char

    if temp:
        result.append(reverse_words(temp) if not in_parentheses else temp)
        
    """if mystr[-1] != result[-1]:
        mystr += ''.join(result) + str(mystr[-1])"""
        
    mystr=''.join(result)+")"  

    return mystr

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")












