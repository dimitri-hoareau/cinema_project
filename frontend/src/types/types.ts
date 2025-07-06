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
  release_date: string;
  evaluation: number;
  status: string;
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

export const FilmStatus = {
  RELEASED: "Released",
  PROJECT: "Project",
  ARCHIVED: "Archived",
} as const;

export type FilmStatusType = (typeof FilmStatus)[keyof typeof FilmStatus];
