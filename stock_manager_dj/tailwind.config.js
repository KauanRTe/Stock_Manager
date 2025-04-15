module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/**/*.{html,js}",
    "./static/css/**/*.css"
  ],
  safelist: [
    'bg-black',
    'text-white',
    'hover:bg-red-500',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
