/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Fira Sans"', 'Arial', 'sans-serif'],
        heading: ['Montserrat', 'sans-serif'],
      }
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        rascals: {
          "primary": "#ffffff",
          "secondary": "#999999",
          "base-100": "#000000",   // Her site is pitch black
          "base-200": "#111111",
          "base-300": "#222222",
          "base-content": "#ffffff", // Pure white text
        },
      }
    ],
  },
}