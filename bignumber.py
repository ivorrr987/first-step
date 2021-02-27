# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:16:22 2021

@author: gibaek
"""

def solution(number, k):
    answer = ''

    number=list(number)
    deleted_number=number.copy()

    max_num='0'
    max_index = 0

    count = 0

    a=len(number)-k


    while a>=1:
       
        
        for i in range(len(deleted_number)-a,-1,-1):
            if max_num <= deleted_number[i]:
                max_num = deleted_number[i]
                max_index = i
               
        for i in range(count, count+max_index+1):
            if number[i] in deleted_number:
                
                deleted_number.remove(number[i]) 
                count+=1
                        
        answer+=number[len(number)-len(deleted_number)-1]
    
        max_num='0'
        max_index = 0
        
        a-=1
        
        
    return answer

    
print(solution("1924", 2))
