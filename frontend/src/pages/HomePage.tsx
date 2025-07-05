import type { Film, FilmStatusType } from "../types/types";
import { type SelectOption } from "../components/ui/CustomSelector";
import { useState, useEffect } from "react";
import { getFilms } from "../api/filmApi";
import { FilmStatus } from "../types/types";
import CustomSelector from "../components/ui/CustomSelector";

const HomePage = () => {
  const [films, setFilms] = useState<Film[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filmStatus, setFilmStatus] = useState<FilmStatusType | "">("");

  const statusOptions: SelectOption<FilmStatusType | "">[] = [
    { value: "", label: "All" },
    { value: FilmStatus.RELEASED, label: "Released" },
    { value: FilmStatus.PROJECT, label: "Project" },
    { value: FilmStatus.ARCHIVED, label: "Archived" },
  ];

  useEffect(() => {
    alert("effect");
    const fetchFilms = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const data = await getFilms(filmStatus);
        setFilms(data);
        console.log(films);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchFilms();
  }, [filmStatus]);

  return (
    <div>
      <h2>Movie list</h2>
      <CustomSelector<FilmStatusType | "">
        value={filmStatus}
        onChange={(newStatus) => setFilmStatus(newStatus)}
        options={statusOptions}
      />

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
              <p>{film.status}</p>
              <p>{film.author.name}</p>
              <img src={film.poster_thumbnail} alt="poster film" />
              <p>{film.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default HomePage;
