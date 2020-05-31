<template>
    <div class="nav">
        <div class="contents">
          <v-row justify="space-btween">
            <v-col cols="12" sm="6" md="2">
              <router-link to="/"><h1>Faker</h1></router-link>
            </v-col>
            <v-col cols="12" sm="6" md="2">
              <router-link to="/login"> <button @click="signIn">Sign In</button> </router-link>
              <button @click="signUp">Get started</button>
            </v-col>
          </v-row>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Nav',
  data () {
    return {

    }
  },
  methods: {
    signIn () {

    },
    signUp () {

    }
  }
}
</script>
<style>
.nav {
    position:relative;
    overflow: hidden;
    display: block;
    width:100%;
    height: 90px;
    color: #fff;
    border-bottom: 1px solid #aaa;

}
.nav .contents{
    /* margin-left: 5%; */
    width:90%;
    height: 90px;
    background: #aaa;
    color:#fff;
    overflow: hidden;
    position: relative;
    margin:0 auto;
}
.contents .h1{
  float: left;
}

</style>
