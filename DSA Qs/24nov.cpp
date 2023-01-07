#include <iostream>
using namespace std;

void print(int arr[],int size){
    for (int i = 0; i < size; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

void dsort(int arr[],int size){
    int low = 0;
    int high = size-1;
    while (low<high)
    {
        while(arr[low]==0)
            low++;
        while (arr[high]==1)
            high--;
        
        if (low<high)
        {
            swap(arr[low],arr[high]);
        }
        
    }
    print(arr,size);
}


void tsort(int arr[],int size){
    int low = 0;
    int mid = 0;
    int high = size-1;
    while (mid<=high)
    {
        switch (arr[mid])
        {
        case 0:
            swap(arr[low],arr[mid]);
            low++,mid++;
            break;
        
        case 1:
            mid++;
            break;
        
        case 2:
            swap(arr[high],arr[mid]);
            high--,mid;            
            break;
        
        }
        
    }
    print(arr,size);
}


int main(){
    int arr[] = {1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1};
    // dsort(arr,sizeof(arr)/sizeof(int));
    int arr2[10]={1,0,2,0,1,0,0,2,1,0};
    tsort(arr2,10);
    return 0;
}