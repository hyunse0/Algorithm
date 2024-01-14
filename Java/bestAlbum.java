import java.util.*;
import java.util.stream.Collectors;

public class bestAlbum {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreCnt = new HashMap<>();
        Map<String, List> genreBymusic = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            genreCnt.put(genres[i], genreCnt.getOrDefault(genres[i], 0) + plays[i]);

            int[] playsByIdx = {i, plays[i]};
            List<int[]> musicList = genreBymusic.getOrDefault(genres[i], new ArrayList());
            musicList.add(playsByIdx);
            genreBymusic.put(genres[i], musicList);
        }

        List<String> genreList = genreCnt.entrySet()
                .stream()
                .sorted((e1, e2) -> e2.getValue() - e1.getValue())
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        List<Integer> answer = new ArrayList<>();
        for (String genre : genreList) {
            List<Integer> musicList = ((List<int[]>) genreBymusic.get(genre))
                    .stream()
                    .sorted(Comparator.comparingInt((int[] arr) -> arr[1]).reversed())
                    .map(arr -> arr[0])
                    .collect(Collectors.toList());

            answer.add(musicList.get(0));
            if (musicList.size() > 1) {
                answer.add(musicList.get(1));
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        bestAlbum s = new bestAlbum();
        System.out.println(s.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500}));
    }
}

