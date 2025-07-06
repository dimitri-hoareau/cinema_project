type StarRatingProps = {
  rating: number;
  maxRating?: number;
};

const StarRating = ({ rating, maxRating = 5 }: StarRatingProps) => {
  return (
    <div className="star-rating">
      {[...Array(maxRating)].map((_, index) => {
        const starValue = index + 1;
        return <span key={starValue}>{starValue <= rating ? "★" : "☆"}</span>;
      })}
    </div>
  );
};

export default StarRating;
