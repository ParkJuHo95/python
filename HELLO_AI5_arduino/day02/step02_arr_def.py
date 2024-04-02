def muteCut(arr,height):
    fi = 0 
    fe = len(arr)-2
    
    while True :
        if arr[fi] > height:
            break
        else :
            fi += 1

    while True :
        if arr[fe] > height:
            break
        else :
            fe -= 1
    
    arr_cut = arr[fi-1:fe+2]
    
    return arr_cut

if __name__ == '__main__':
    arr = [ 0,0,0,0,0,0,5,6,7,8,5,4,0,0,0,0,0]
    mine = muteCut(arr,2)
    print(mine)

            
    