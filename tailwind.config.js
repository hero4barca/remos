/** @type {import('tailwindcss').Config} */
module.exports = {
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
