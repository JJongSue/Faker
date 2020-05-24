<template>
    <div class="nav">
        <div class="contents">
            <router-link
                to="/login">
           <button @click="signIn">Sign In</button>
            </router-link>
           <button @click="signUp">Get started</button>
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
    margin-left: 5%;
    width:90%;
    height: 90px;
    background: #aaa;
    color:#fff;
    position: absolute;
}
</style>
