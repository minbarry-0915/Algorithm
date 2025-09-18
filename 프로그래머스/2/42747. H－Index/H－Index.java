import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);  // 오름차순
        int n = citations.length;
        int left = 0;
        int right = n - 1;
        int maxH = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            int h = n - mid;  // 남은 논문 수

            if (citations[mid] >= h) {
                maxH = h;
                right = mid - 1;  // 더 작은 index 확인
            } else {
                left = mid + 1;   // 더 큰 index 확인
            }
        }

        return maxH;
    }
}
