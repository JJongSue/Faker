import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView'
import MakeMovieView from '../views/MakeMovieView'
import SignInView from '../views/SignInView'
import SignUpView from '../views/SignUpView'
Vue.use(VueRouter);

export const router =  new VueRouter({
    mode: 'history',
    routes:[
        {
            path: '/',
            component: HomeView
        },
        {
            path: '/signIn',
            component: SignInView
        },
        {
            path: '/signUp',
            component: SignUpView
        },
        {
            path: '/makeMovie',
            component: MakeMovieView
        }
    ]
})
