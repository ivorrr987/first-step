# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:58:56 2021

@author: gibaek
"""

def solution(n, lost, reserve):
    answer = 0
    duplicated =  0
    matching = 0
    
    
    duplicated_value=[]
    
    
    matched_lost=[]
    matched_reserve=[]
    
    length_of_lost=len(lost)
    
    lost.sort()
    reserve.sort()
    
   
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j]:
                duplicated += 1
                duplicated_value.append(lost[i])
                
    for i in range(len(duplicated_value)):
        lost.remove(duplicated_value[i])
        reserve.remove(duplicated_value[i])
    
    print('duplicated_value is', duplicated_value)
    print('lost is', lost)
    print('reserve is', reserve)
    
    

    for i in range(len(lost)):
        for j in range(len(reserve)):             
              if reserve[j]==(lost[i]-1) or reserve[j]==(lost[i]+1):
                if (reserve[j] not in matched_reserve) and (lost[i] not in matched_lost):
                    matching += 1
                    matched_lost.append(lost[i])
                    matched_reserve.append(reserve[j])
        
   
    answer= n - (length_of_lost-duplicated-matching)
                            
    
    print('n is', n)
    print('length of lost is', len(lost))
    print('length of reserve is', len(reserve))
    print('duplicated is', duplicated )
    print('matching is', matching )
    print('matched_lost is', matched_lost)
    print('matched_reserve is', matched_reserve)
    print('answer is' ,answer)

    return answer

solution(10, [1,2,3,5,7,8,9], [1, 3, 4, 8, 9])


