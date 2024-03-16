import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import User from '../views/User.vue'
import Login from '../views/login'
import Main from '../views/main'
import Train from '../views/train'
import Forecast from '../views/forecast'
import Show from '../views/show'



Vue.use(VueRouter)

const routes = [
  //主路由
  {
    path: '/',
    component: Main,
    name:'home',
    redirect: '/home',
    children: [
      { path: '/home', component: Home },//首页
      { path: '/user', component: User },//用户
      { path: '/train', component: Train },//模型训练
      { path: '/forecast', component: Forecast },//预测
      { path: '/show', component: Show }//结果展示
    ]
  },
  {
    path: '/login',
    name:'login',
    component: Login
  }//登录
]

const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

export default router


