import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/accounts/Login.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/accounts/Signup.vue')
  },
  {
    path: '/findidpw',
    name: 'FindIdPw',
    component: () => import('../views/accounts/FindIdPw.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),    
    // 상단바와 하단바가 있는 views는 아래에 children으로 등록되어야 합니다.
    children: [
      {
        path: '',
        name: 'Main',
        component: () => import('../views/Main.vue')
      },
      {
        path: '/diary',
        name: 'Diary',
        component: () => import('../views/Diary.vue')
      },
      {
        path: '/selectoption',
        name: 'SelectOption',
        component: () => import('../views/courses/SelectOption.vue')
      },
      {
        path: '/travelingcourse',
        name: 'TravelingCourse',
        component: () => import('../views/courses/TravelingCourse.vue')
      },
      // {
      //   path: '',
      //   name: 'Main',
      //   component: () => import('../views/Main.vue')
      // },
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
