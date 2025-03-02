
def rotate(lst,k):
    print("Input Array", lst)
    lst.reverse()
    print(lst)
    lst[k:] = reversed(lst[k:])
    print(lst[k:])
    lst[:k] = reversed(lst[:k])
    print(lst[:k])
    print("Final Rotated Array ", lst)



if __name__ == '__main__':
    rotate([1,2,3,4,5,6],2)
