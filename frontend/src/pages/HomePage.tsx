import type { Film } from "../types/types";
import { useState, useEffect } from "react";
import { getFilms } from "../api/filmApi";

const HomePage = () => {
  const [films, setFilms] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFilms = async () => {
      try {
        setIsLoading(true);
        const data = await getFilms();
        console.log(data);
        if (data) {
          setFilms(data);
          console.log(films);
        }
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchFilms();
  }, []);

  console.log(films);
  return (
    <div>
      <h2>Movie list</h2>

      {isLoading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error : {error}</p>
      ) : (
        <ul>
          {films.map((film: Film) => (
            <li key={film.id}>
              <h3>{film.title}</h3>
              <p>{film.released_date}</p>
              <p>{film.evaluation}</p>
              <p>{film.statut}</p>
              <p>{film.author.name}</p>
              <img src={film.poster_thumbnail} alt="poster film" />
              <p>{film.description}</p>:
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default HomePage;
