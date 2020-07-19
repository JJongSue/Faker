<template>
  <v-app>
  <div id="app">
    <Nav></Nav>

    <router-view/>

  </div>
  </v-app>
</template>

<script>
import Nav from './components/Nav'

export default {
  name: 'App',
  components: {
    Nav

  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #aaa;
  background: #000;
  padding:0;
  margin:0;
  width:100%;
  margin:0 auto;
  height: 100vh;
}
Nav{
  width:100%;
  height: 90px;
}

</style>
