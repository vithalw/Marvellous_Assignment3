def getFrequency(arr,number):
    count=int(0);
    for i in range(0,len(arr),1):
        if(arr[i]==number):
            count=count+1;
    return count;        



def main():
    size=int(input("Enter size of List: "))
    arr=[];
    print("Enter elements: ")
    element=int(0);
    for i in range(0,size,1):
        element=int(input());
        arr.append(element);
    number=int(input("Enter any number: "));
    print("Frequency is: ",getFrequency(arr,number));    
    

if __name__=="__main__":
    main();
