import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
const app = createApp(App)
axios.defaults.baseURL = "http://localhost:8000"
app.config.globalProperties.$axios = axios

app.mount('#app')
 <template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
}
</script>

<style lang="less" >
  html,body,h3{
    margin:0;
    padding:0;
  }
</style>