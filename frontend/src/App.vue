<template>
  <div id="app">
    <tool-bar></tool-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import ToolBar from './components/ToolBar'
export default {
  name: 'App',
  components: {
    ToolBar,
  }
}
</script>

<style>
body{
  padding:0; 
  margin: 0; 
}
#app {

}
</style>
