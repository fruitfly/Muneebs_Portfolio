package sorting;

//This class contains methods for sorting arrays of integers
public class Sorting {

    //Returns a random array of numElements integers up to size maxValue
    public static int[] makeRandomArray(int numElements, int maxValue) {
        int[] x = new int[numElements]; //create an empty array

        for (int i = 0; i < numElements; i++) {
            double multiplier = Math.random(); //a random decimal between 0 and 1
            x[i] = (int) (multiplier * maxValue); //a random integer between 0 and maxValue
        }

        return x; //returns the filled array
    }

    //Prints the elements of the array a from left to right
    public static void displayArray(int[] a) {
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + "  ");
        }

        System.out.println("\n");
    }

    //Sorts the array a using the Bubble Sort algorithm
    public static void bubbleSort(int[] a) {
        int n = a.length;

        System.out.println("ORIGINAL ARRAY: ");
        displayArray(a);

        for (int i = 1; i < n; i++) { //Do n-1 passes through the array
            System.out.println("PASS #" + i);
            System.out.println("--------");

            for (int j = 0; j < n - i; j++) { //In the current pass i, compare each adjacent pair of values in the array, and swap if needed

                if (a[j] > a[j + 1]) {
                    swap(a, j, j + 1); //swap element j with its neighbour to the right
                }

                displayArray(a);
            }
        }
    }

    
    //Sorts the array a using the Insertion Sort algorithm
    public static void insertionSort(int[] a) {
        //CODE THIS
        System.out.println("ORIGINAL ARRAY: ");
        displayArray(a);
        for (int i=1;i<a.length;i++){
            System.out.println("PASS #" + i);
            System.out.println("--------");
            displayArray(a);
            int j= i;
            while(j>0 && a[j-1]>a[j]){
                Sorting.swap(a, j-1, j);
                j-=1;
                
                        
            }
        }
        System.out.println("FINAL PASS");
        System.out.println("--------");
        displayArray(a);
        
    }
    
    
    

    
    //Swaps element i with j in the array a
    public static void swap(int[] a, int i, int j) {
        int temp = a[i]; //a temporary variable to hold the original value of a[i]
        a[i] = a[j];     //reassign a[i] to a[j]'s original value
        a[j] = temp;     //reassign a[j] to a[i]'s original value, which was recorded by temp
    }

    
    public static void main(String[] args) {

        int[] x = makeRandomArray(8, 200); //a random array of 8 integers up to size 100
        bubbleSort(x); //sort array x using the bubble-sort algorithm
        
        int[] y = makeRandomArray(8,200);
        insertionSort(y);

        
        

    }
}
