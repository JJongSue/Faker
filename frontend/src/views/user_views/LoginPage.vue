<template>
    <div id="login">
        <form action="submit">
            <input type="text" v-model="id">
            <input type="password" v-model="password">
            <button >Login</button>
        </form>
    </div>
</template>

<script>
import http from '../../../http-common'

export default {
  data () {
    return {
      id: '',
      password: ''
    }
  },
  methods: {
    login () {
      http
        .post('/user/login', {

        }).then(Response => {

        })
        .catch((err) => {
          console.log(err)
          alert('로그인에 실패하였습니다.')
        })
    }
  }

}
</script>

<style>

</style>
