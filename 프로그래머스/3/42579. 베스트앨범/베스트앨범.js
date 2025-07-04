function solution(genres, plays) {
    const genreWithPlays = genres.map((genre, index) => (
    {genre, plays: plays[index], index}
    ));
    
    const genrePlayCount = {};
    for (const {genre, plays} of genreWithPlays){
        genrePlayCount[genre] = (genrePlayCount[genre] || 0) + plays;
    }
    
    const sortedGenres = Object.keys(genrePlayCount).sort(
    (a,b) => genrePlayCount[b] - genrePlayCount[a]
    )
    
    const result = [];
    for (const genre of sortedGenres){
        const songInGenre = genreWithPlays.filter(song => song.genre === genre).sort((a,b) => b.plays - a.plays || a.index - b.index);
        result.push(...songInGenre.slice(0,2).map(song => song.index));
        
    }
    
    return result
    
    
}