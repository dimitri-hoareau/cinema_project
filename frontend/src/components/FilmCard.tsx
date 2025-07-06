import type { Film } from "../types/types";
import { Link } from "react-router-dom";
import StarRating from "./ui/StarRating";
import "../styles/components/_film-card.scss";

type FilmCardProps = {
  film: Film;
};

const FilmCard = ({ film }: FilmCardProps) => {
  return (
    <li className="film-card">
      <Link to={`/films/${film.id}`} className="film-card__link">
        <img
          loading="lazy"
          src={film.poster_thumbnail}
          alt={`Affiche du film ${film.title}`}
          className="film-card__poster"
        />
        <div className="film-card__overlay">
          <div className="film-card__row">
            <h3 className="film-card__title">{film.title}</h3>
            <span className="film-card__status">{film.status}</span>
          </div>
          <div className="film-card__row  film-card__row--bottom">
            <span className="film-card__date">
              {film.release_date
                ? new Date(film.release_date).getFullYear()
                : "N/A"}
            </span>
            <div className="film-card__evaluation">
              <StarRating rating={film.evaluation} />
            </div>
          </div>
        </div>
      </Link>
    </li>
  );
};

export default FilmCard;
