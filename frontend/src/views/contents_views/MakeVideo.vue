<template>
   <div id="make-video">
        <v-file-input
            accept="image/png, image/jpeg, image/bmp"
            placeholder="이미지 입력"
            prepend-icon="camera"
            label="Avatar"
            dark
        ></v-file-input>
      <v-file-input
            accept="video/*"
            placeholder="비디오 입력"
            prepend-icon="camera"
            label="Avatar"
            dark
        ></v-file-input>
        <v-btn>전송</v-btn>
        <div class="player-container" style="width:1000px; height:500px; margin: 0 auto">
          <vue-core-video-player src='../../src/assets/ssafy.mp4' :autoplay=true ></vue-core-video-player>
        </div>

   </div>
</template>

<script>

import VueCoreVideoPlayer from 'vue-core-video-player'
import Vue from 'vue'
Vue.use(VueCoreVideoPlayer)
export default {
  methods: {

  }
}
</script>

<style>

</style>
