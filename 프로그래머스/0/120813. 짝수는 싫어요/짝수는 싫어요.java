class Solution {
    public int[] solution(int n) {
        int len = (n%2==0)? n/2 : n/2+1;
        int[] answer = new int[len];
        
        int num = 1;
        for (int i=0; i<len; i++){
            answer[i] = num;
            num += 2;
        }
        
        return answer;
    }
}