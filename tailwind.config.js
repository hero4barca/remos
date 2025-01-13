/** @type {import('tailwindcss').Config} */
module.exports = {
  important: true, // Ensures Tailwind's utilities take precedence
  content: [
    './**/templates/*.html',
    './project/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Source Serif Pro"', 'serif'], // Adds the font to the serif stack
      },
    },
  },
  plugins: [],
}
