<template>
  <div class="home">
    <Player />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Player from '@/components/Player.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'Home',
  components: {
    Player,
  },
});
</script>
