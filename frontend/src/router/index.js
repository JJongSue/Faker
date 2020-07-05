import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/user_views/LoginPage'
import Home from '@/views/Home'
import MakeImagePage from '@/views/contents_views/MakeImage'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/make/image',
      name: 'make_image',
      component: MakeImagePage
    }
  ]
})
