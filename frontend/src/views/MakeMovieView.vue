<template>
<div>
  <div>make movie</div>

  <label for="avatar">Choose a picture:</label>
  <input type="file"
        id="avatar" name="avatar"
        accept="image/png, image/jpeg">
  

  <label for="avatar">Choose a video:</label>
  <input type="file"
        id="avatar" name="avatar"
        accept="video/*">
</div>
</template>

<script>
import { postAIData } from '../api/index'
export default {
  data(){
    return{

    }
  },
  methods:{
    postAIData(){
      postAIData()
        .then(response=>{
          console.log(response);
        })
        .catch(error=>{
          console.log(error);
        })
    }

  }
}
</script>

<style>

</style>
