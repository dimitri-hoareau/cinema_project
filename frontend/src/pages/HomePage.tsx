import type { Film, FilmStatusType } from "../types/types";
import { type SelectOption } from "../components/ui/CustomSelector";
import { useState, useEffect } from "react";
import { getFilms } from "../api/filmApi";
import { FilmStatus } from "../types/types";
import CustomSelector from "../components/ui/CustomSelector";
import FilmCard from "../components/FilmCard";
import "../styles/components/_film.scss";

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
    const fetchFilms = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const data = await getFilms(filmStatus);
        setFilms(data);
        console.log(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchFilms();
  }, [filmStatus]);

  return (
    <div className="film-container">
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
        <ul className="film-container__list">
          {films.map((film) => (
            <FilmCard key={film.id} film={film} />
          ))}
        </ul>
      )}
    </div>
  );
};

export default HomePage;
