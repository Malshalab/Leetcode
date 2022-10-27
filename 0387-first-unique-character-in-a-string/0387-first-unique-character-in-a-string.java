class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> counts= new HashMap() ;
        
        for(int i =0 ; i<s.length();i++){
            char c=s.charAt(i) ;
            if(counts.containsKey(c)){
                counts.put(c,counts.get(c)+1) ;
            }
            else{
                counts.put(c,1) ;
            }
        }
        
        for(int i=0 ; i<s.length(); i++){
            char c=s.charAt(i);
            if(counts.get(c)==1){
                return i;
            }   
        }
        return -1 ;
    }
}