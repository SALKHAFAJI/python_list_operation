
import random


class main_list():

    empty_list = []

    # to find the max number in list we can
    # use max() function in python
    
    def length(ml):
        counter = 0
        for i in ml:
            counter += 1
        return counter
    def count_elem(ml, element):
        counter = 0
        for i in ml:
            if i == element:
                counter += 1
        return counter
    
    def extend_list(ml1, ml2):
        return ml1 + ml2

    def show(ml):
        print(ml)

    def findMax(input_list):

        mout = input_list[0]
        for i in input_list:
            if i >= mout:
                mout = i
        return mout

    def findMin(input_list):

        mout = input_list[0]
        for i in input_list:
            if i <= mout:
                mout = i
        return mout
    def sort(input_list):

        out_list = []

        for i in range(len(input_list)):

            #find biggest number in list
            big = main_list.findMax(input_list)

            #add the biggest number to new list at position [0]
            out_list.insert(0, big)

            #remove the bigest number from old list
            input_list.remove(big)

        return out_list

    def random_element(mylist):
        for i in range(20):
            mylist.append(random.randint(0,20))

    def add(input_list, *element):
        for i in element:
            input_list += [i]

    def remove_elem(input_list, *element):
        for i in element:
            if i in input_list:
                start = input_list[:input_list.index(i)]
                end = input_list[input_list.index(i) + 1 :]
            input_list = start + end
        return input_list
    
    def another_remove(input_list, *elem):
        news = [] 
        for i in input_list:
            if i in elem:
                pass
            else:
                news.append(i)
        return news
    def pop_position(input_list, *position):
        for i in position:
            start = input_list[ : i]
            end = input_list[i + 1 :]
            input_list = start + end
        return input_list
    
    def sum_all(input_list):
        out = 0
        for i in input_list:
            out += i
        return i

    def revers_elem(input_list):
        
        out_list = []
        for i in input_list:
            out_list.insert(0 ,i)
        return out_list
        
    def insert_elem(in_list, element, pos):
        element = [element]
        start = in_list[ : int(pos)]
        end = in_list[int(pos) :]
        out_list = start + element + end
        return out_list

    def copy_list(input_list):
        out = []
        for i in input_list:
            out.append(i)
        return out
    
    def index_elem(input_list, element, seq):
        counter = 0
        pos = -1
        for i in input_list:
            pos += 1
            if i == element:
                counter += 1
                if counter == seq:
                    return pos

if __name__ == "__main__":

    ml = main_list.empty_list
    main_list.show(ml)
    print(ml)
    main_list.random_element(ml)
    print(ml)
    ml =  main_list.sort(ml)
    print(ml)
    main_list.add(ml, 99,88,77,5,5,5,5)
    print(ml)
    ml = main_list.remove_elem(ml,88)
    print(ml)
    ml = main_list.pop_position(ml, 1,0,2)
    print(ml)
    print("this is pos : " + str(main_list.index_elem(ml,5,2)))
    print(main_list.sum_all(ml))
    print(main_list.findMax(ml))
    print(main_list.findMin(ml))
    #print(main_list.revers_elem(ml))
    print(ml)
    ml = main_list.insert_elem(ml, 9999999, 3)
    print(ml)
    ml = main_list.revers_elem(ml)
    print(ml)
