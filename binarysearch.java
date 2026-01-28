//leetcode @34
public class binarysearch {
    public static void main(String[] args) {
        int arr[] = { 2, 2, 3, 4, 4, 4, 6, 8, 9 };
        int res[] = new int[2]; // of size 2
        int first = binarySearch(arr, 4, true);
        int last = binarySearch(arr, 4, false);
        if (first == -1) {
            System.out.println("Occurrance of target is : " + 0);
        } else {
            System.out.println("Ocurrance of target is : " + (last - first + 1)); // If we subtract first from last, we
                                                                                  // only
            // get the difference between the indices,
            // which is one less than the actual
        } // count.
        res[0] = first;
        res[1] = last;
    }

    static int binarySearch(int arr[], int target, boolean isFirst) {
        int ans = -1;
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] == target) {
                ans = mid;
                if (isFirst) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return ans;

        // if (ans == -1) {
        // System.out.println("Element not found");
        // } else {
        // System.out.println("Element found " + target + " at index " + ans);
        // }
    }
}
