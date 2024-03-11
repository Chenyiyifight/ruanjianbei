import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import store from './store'

import ECharts from 'vue-echarts'; // 引入 vue-echarts
import 'echarts';
Vue.component('v-chart', ECharts); // 注册组件

Vue.use(ElementUI)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
