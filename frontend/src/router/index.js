import { createRouter, createWebHistory } from 'vue-router';

// 导入你的页面组件
import Home from '../App.vue';
import Info from '../components/Info.vue';
import Announcement from '../components/Announcement.vue';
import Login from '../components/Login.vue';
import Guide from '../components/Guide.vue';

// 配置路由
const routes = [
  { path: '/', redirect: '/Info' }, // 默认重定向到 Info
  { path: '/Info', name: 'Info', component: Info }, // 信息展示
  { path: '/Announcement', name: 'Announcement', component: Announcement }, // 竞赛公示
  { path: '/Login', name: 'Login', component: Login }, // 登录
  { path: '/Guide', name: 'Guide', component: Guide } // 使用指南
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes, // 将配置的路由传递给路由实例
});

export default router;
