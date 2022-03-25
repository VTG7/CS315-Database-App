module.exports = {
  content: ["src/App.js", 'src/components/**/*.{html,js}'],
  theme: {
    extend: {
    },
  },
  plugins: [require('@tailwindcss/forms')],
}
