export interface Author {
  id: number;
  nom: string;
  email: string;
  date_de_naissance: string;
  films?: Film[];
}

export interface Film {
  id: number;
  titre: string;
  description: string;
  date_de_sortie: string;
  evaluation: number;
  statut: string;
  source: string;
  created_at: string;
  auteur_associe: Author;
}

export interface Spectator {
  id: number;
  email: string;
  username: string;
  bio?: string;
  avatar?: string;
  films_favoris?: Film[];
}
