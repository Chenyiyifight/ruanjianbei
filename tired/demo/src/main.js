import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import store from './store'

import ECharts from 'vue-echarts'; // 引入 vue-echarts
import 'echarts';
import ecStat from 'echarts-stat';

import './api/mock'
import Cookie from 'js-cookie'

Vue.component('v-chart', ECharts); // 注册组件

Vue.use(ElementUI)

//全局前置导航守卫
router.beforeEach((to, from, next) => {
  //判断token是否存在
  const token = Cookie.get('token')
  if(!token&&to.name !=='login'){
    next({name:'login'})
  }else if(token&&to.name=='login'){
    next({name:'home'})
  }else{
    next();
  }
})


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
