<template>
    <div class="nav">
        <div class="contents">
          <v-row >
            <v-col :class="`d-flex justify-start mb-6`">
              <router-link to="/"><h1>Faker</h1></router-link>
            </v-col>
            <v-col :class="`d-flex justify-center mb-6 ` "  >
              <router-link to="/make/image"><h3>Make Image</h3></router-link>
            </v-col>
            <v-col :class="`d-flex justify-center mb-6`">
              <router-link to="/make/video"><h3>Make video</h3></router-link>
            </v-col>
            <v-col :class="`d-flex justify-end mb-6`">
              <router-link to="/login">Sign In</router-link>

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
      activeItem: 'about'
    }
  },
  methods: {
    signIn () {

    },
    signUp () {

    },
    isActive: function (menuItem) {
      return this.activeItem === menuItem
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
    /* background: #aaa; */
    color:#fff;
    overflow: hidden;
    position: relative;
    margin:0 auto;
}
.nav .contents h1{
   color : #ffb917 !important;
}
.nav .contents a{
  text-decoration: none ;
  color: #6B6B6B;
  line-height: 90px;
}
.nav .contents a:hover{
  color: #ffffff;
}

.nav .contents .router-link-active {
  color : #ffffff;
}
.nav .contents .col{
  padding-top: 0px !important;
}

.nav .contents h3{
  /* height: 90px; */

 vertical-align: middle;
}
</style>
