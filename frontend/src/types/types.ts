export interface Author {
  id: number;
  name: string;
  email: string;
  birth_date: string;
  films?: Film[];
}

export interface Film {
  id: number;
  title: string;
  description: string;
  released_date: string;
  evaluation: number;
  statut: string;
  source: string;
  created_at: string;
  author: Author;
  poster_thumbnail: string;
  backdrop_path: string;
}

export interface Spectator {
  id: number;
  email?: string;
  username: string;
  bio?: string;
  avatar?: string;
  films_favoris?: Film[];
}

export interface MyJwtPayload {
  user_id: number;
  username: string;
  exp: number;
}
