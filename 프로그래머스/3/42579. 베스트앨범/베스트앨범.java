import java.util.*;

class Song{
    int index;
    int play;
    
    Song(int index, int play){
        this.index = index;
        this.play = play;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreTotal = new HashMap<>();
        Map<String, List<Song>> genreSongs = new HashMap<>();
        
        int n = genres.length;
        
        for(int i = 0; i < n ; i ++){
            String genre = genres[i];
            int play = plays[i];
            
            genreTotal.put(genre, genreTotal.getOrDefault(genre, 0) + play);
            
            genreSongs.putIfAbsent(genre, new ArrayList<>());
            genreSongs.get(genre).add(new Song(i, play));
        }
        
        List<String> genreOrder = new ArrayList<>(genreTotal.keySet());
        genreOrder.sort((a,b) -> genreTotal.get(b) - genreTotal.get(a));
        
        List<Integer> answerList = new ArrayList<>();
        for (String genre: genreOrder){
            List<Song> list = genreSongs.get(genre);
            
            list.sort((s1, s2) -> s1.play == s2.play ? s1.index - s2.index : s2.play - s1.play);
            for (int i = 0; i < Math.min(2, list.size()); i ++){
                answerList.add(list.get(i).index);
            }
        }
        return answerList.stream().mapToInt(i -> i).toArray();
    }
}