/** @type {import('tailwindcss').Config} */
module.exports = {
  important: true, // Ensures Tailwind's utilities take precedence
  content: [
    './**/templates/*.html',
    './project/templates/**/*.html',
  ],
  theme: {
    extend: {
      screens: {
        mdTo1160: { raw: "(min-width: 768px) and (max-width: 1160px)" }, // Custom range
        lgTo1160: { raw: "(min-width: 1024px) and (max-width: 1160px)" }, // Custom range
        lgTo1220: { raw: "(min-width: 1024px) and (max-width: 1220px)" }, // about team section
        lgTo1325: { raw: "(min-width: 1024px) and (max-width: 1325px)" }, // about team section
      },
      fontFamily: {
        serif: ['"Source Serif Pro"', 'serif'], // Adds the font to the serif stack
      },
    },
  },
  plugins: [],
}
