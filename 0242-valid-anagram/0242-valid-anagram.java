class Solution {
    public boolean isAnagram(String s, String t) {
        List<Character> arr1 = new ArrayList<>();
        List<Character> arr2 = new ArrayList<>();
        for(char c: s.toCharArray()){
            arr1.add(c);
        }
        for(char c: t.toCharArray()){
            arr2.add(c);
        }
        Collections.sort(arr1);
        Collections.sort(arr2);
        return arr1.equals(arr2);

        
    }
}