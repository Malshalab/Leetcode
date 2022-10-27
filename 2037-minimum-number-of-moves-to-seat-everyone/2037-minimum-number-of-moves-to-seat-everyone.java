class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats) ;
        Arrays.sort(students) ;
        int result=0 ;
        for(int i =0 ; i<students.length ;i++){
            result =result+ Math.abs(seats[i]-students[i]) ;
        }
        return result ;
    }
}