class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> char_countsOne=new HashMap() ;
        HashMap<Character,Integer> char_countsTwo=new HashMap() ;
        for(int i=0; i<s.length();i++){
            char c=s.charAt(i) ;
            
            if(char_countsOne.containsKey(c)){
                char_countsOne.put(c,char_countsOne.get(c)+1) ;
            } else {
                char_countsOne.put(c,1);
            }
        }
        
        for(int i=0; i<t.length();i++){
            char c=t.charAt(i) ;
            
            if(char_countsTwo.containsKey(c)){
                char_countsTwo.put(c,char_countsTwo.get(c)+1) ;
            } else {
                char_countsTwo.put(c,1);
            }
        }
        
        if(char_countsOne.equals(char_countsTwo)){
            return true ;
        }
        return false ;
    }
}