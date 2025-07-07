// src/components/layout/Footer.test.tsx

import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import Footer from "./Footer";

describe("Footer Component", () => {
  it("Display copyright and current year", () => {
    render(<Footer />);

    const currentYear = new Date().getFullYear();

    const footerElement = screen.getByRole("contentinfo");

    expect(footerElement).toHaveTextContent(
      `© ${currentYear} CinéApp - All rights reserved.`
    );
  });
});
