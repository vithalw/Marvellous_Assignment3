def getMax(arr):
    return max(arr);

def main():
    size=int(input("Enter size of List: "))
    arr=[];
    print("Enter elements: ")
    element=int(0);
    for i in range(0,size,1):
        element=int(input());
        arr.append(element);
    print("Max is: ",getMax(arr));

if __name__=="__main__":
    main();
