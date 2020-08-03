<template>
  <div class="header">
      <router-link to="/home">Home</router-link> |
      <router-link to="/makeMovie">이미지 합성하기</router-link> | 
      <router-link to="/signIn">Sign in</router-link> | 
      <router-link to="/signUp">Sign up</router-link> 
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.header{
    color: white;
    background: #24292e;
    display: flex;
    padding: 8px;
}
.header a {
    color: white;
    text-decoration: none;
}
.header .router-link-exact-active{
    text-decoration: none;
    color: yellow;

}
</style>