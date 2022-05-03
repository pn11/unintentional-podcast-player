module.exports = {
  pages: {
    index: {
      entry: "src/main.ts",
      title: "Unintended Podcast Player",
    }
  },
  publicPath: process.env.NODE_ENV === 'production'
  ? '/unintentional-podcast-player/'
  : '/'
}
