<template>
  <div class="Player">
    <a href="https://github.com/pn11/unintentional-podcast-player"><img src="@/assets/GitHub-Mark-120px-plus.png" height="20"></a>
    <h1>Unintentional Podcast Player</h1>
    <button v-on:click="getRandomEpisode">Another episode</button><br><br>
    <audio controls
        preload="auto" width="100%" v-bind:type="audio_type" v-bind:src="audio_url">
        <a v-bind:href="audio_url">{{audio_url}}</a>
    </audio><br>
    <h2><a v-bind:href="show_link">{{show_title}}</a></h2>
    <img v-bind:width="imgWidth" v-bind:src="show_cover_url">
    <h3><a v-bind:href="episode_link">{{episode_title}}</a></h3>
    <img v-bind:width="imgWidth" v-bind:src="episode_art_url">
    <p v-html="episode_description_html"></p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
// import episodes_data from "@/assets/episodes.json";

export default defineComponent({
  name: 'Player',
  components: {
  },
  computed: {
  },
  data() {
    return {
      episodes_data: [],
      random_episode: null,
      show_title: '',
      show_link: '',
      show_cover_url: '',
      episode_title: '',
      episode_link: '',
      episode_description: '',
      episode_description_html: '',
      episode_art_url: '',
      audio_url: '',
      audio_type: '',
      imgWidth: "200"
    }
  },
  async created() {
    //const foobar = await this.latest();
    this.episodes_data = require('@/assets/episodes.json');
  },
  methods: {
    getRandomEpisode: function () {
      const array = this.episodes_data;
      this.random_episode = array[Math.floor(Math.random() * array.length)]
    },
  },
  watch: {
    random_episode: function (ep){
      this.show_title = ep.show_title
      this.show_link = ep.show_link
      this.show_cover_url = ep.show_cover_url
      this.episode_title = ep.title
      this.episode_link = ep.link
      this.episode_description = ep.description
      this.episode_description_html = ep.description_html
      this.episode_art_url = ep.episode_art_url
      this.audio_url = ep.enclosures[0].url
      this.audio_type = ep.enclosures[0].mime_type
    }
  },
  beforeMount(){
    this.getRandomEpisode()
  },
});
</script>
