'''Игра угадай число/ Компьютер сам загадывает и угадывает число'''

import numpy as np

def random_predict(number:int=np.random.randint(1,100)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count=0
    max=100
    min=0
    predict_number=np.random.randint(1,100) #предполагаемое число
    
    while True:
        count+=1
        
        if predict_number>number:
            max=predict_number-1
            predict_number=(max+min)//2
        elif predict_number<number:
            min=predict_number+1
            predict_number=(max+min)//2
        else:
            break #выход из цикла eсли угадали
        print(predict_number,number)
    return(count)

def score_game(random_predict) ->int:
    """Среднее количество попыток за 100 подходов угадывает наш алгоритм число 

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls=[]
    np.random.seed(1)#используем сид для воспроизводимости
    random_array=np.random.randint(1,101,size=(250))#загадали список чисел
    print(random_array)
    Print(len(random_array))
    
    i=0                            
    for number in random_array:
        i+=1
        
    count_ls.append(random_predict(number))
    print(count_ls)
    print(i)
        
    score=int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score}попыток')
    return(score)


    score_game(random_predict)

#print(f'Количество попыток:{random_predict(10)}')
