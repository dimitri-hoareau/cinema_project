import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import FilmCard from "./FilmCard";
import type { Film } from "../types/types";
import { MemoryRouter } from "react-router-dom";

describe("FilmCard Component", () => {
  it("Display Film informations", () => {
    const mockFilm: Film = {
      id: 1,
      title: "test film",
      description: "test description",
      poster_thumbnail: "/test-poster.jpg",
      release_date: "2025-01-01",
      status: "Released",

      source: "tmdb",
      created_at: "2025-01-02",
      author: {
        id: 1,
        name: "test author",
        email: "author@gmail.com",
        birth_date: "2005-01-02",
      },

      backdrop_path: "/test-backdrop.jpg",
      evaluation: 0,
    };
    render(
      <MemoryRouter>
        <FilmCard film={mockFilm} />
      </MemoryRouter>
    );

    expect(screen.getByText("test film")).toBeInTheDocument();

    const filmCardImg = screen.getByRole("img");
    expect(filmCardImg).toHaveAttribute("src", "/test-poster.jpg");
  });
});
