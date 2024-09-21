import Vue from 'vue';
import App from './App.vue';
import router from './router';  // 引入路由配置

Vue.config.productionTip = false;

new Vue({
  router,  // 注入路由
  render: h => h(App)
}).$mount('#app');
