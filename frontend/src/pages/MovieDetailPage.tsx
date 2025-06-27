import { useParams } from "react-router-dom";

const MovieDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  return (
    <div>
      <h2>CineApp MovieDetailPage</h2>
      <p>Detail for one movie {id}</p>
    </div>
  );
};

export default MovieDetailPage;
