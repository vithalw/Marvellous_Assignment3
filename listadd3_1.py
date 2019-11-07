def listadd(arr):
    sum=int(0)
    for i in range(0,len(arr),1):
        sum=sum+arr[i]
    return sum    


def main():
    size=int(input("Enter size of List: "))
    arr=[];
    print("Enter elements: ")
    element=int(0);
    for i in range(0,size,1):
        element=int(input());
        arr.append(element);
    print("Addition is: ",listadd(arr));

if __name__=="__main__":
    main();
