<template>
    <div id="make_image">
        <div class="input_image">

        <v-icon class="select-img" large dark>videocam</v-icon>
        <!-- <v-icon>event</v-icon> -->
        <!-- <label for="upload_file">업로드</label> -->
        <!-- <v-icon large dark>image</v-icon> -->
        <v-file-input
            accept="image/png, image/jpeg, image/bmp"
            placeholder="Pick an avatar"
            prepend-icon="camera"
            label="Avatar"
            dark
        ></v-file-input>

        </div>
        <div class="progress">
            <v-progress-linear :dark="true" value="15"></v-progress-linear>
        </div>
    </div>
</template>

<script>
export default {
  data: function () {
    return {
      absolute: false,
      active: true,
      opacity: 0.3,
      bottom: false,
      buffer: 100,
      fixed: false,
      height: 4,
      indeterminate: false,
      query: false,
      rounded: false,
      stream: false,
      striped: false,
      top: false,
      value: 25
    }
  }
}
</script>

<style>
#make_image .input_image{
    width : 100%;
    height: 550px;
    /* background : #aaaa; */
}
#make_image .input_image label {
  display: inline-block;
  padding: .5em .75em;
  color: #fff;
  font-size: inherit;
  line-height: normal;
  vertical-align: middle;
  background-color: #5cb85c;
  cursor: pointer;
  border: 1px solid #4cae4c;
  border-radius: .25em;
  -webkit-transition: background-color 0.2s;
  transition: background-color 0.2s;
}

#make_image .input_image label:hover {
  background-color: #6ed36e;
}

#make_image .input_image label:active {
  background-color: #367c36;
}

#make_image .input_image input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
#make_image .progress{
    width: 100%;
    height : 160px;
    /* background: wheat; */
}
#make_image .progress .row .bar{
    height: 30px;
}
</style>
