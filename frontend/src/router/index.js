import Vue from 'vue';
import Router from 'vue-router';
import InfoView from '@/views/InfoView.vue';
import AnnounceView from '@/views/AnnounceView.vue';
import LoginView from '@/views/LoginView.vue';
import GuideView from '@/views/GuideView.vue';
import UserView from "@/views/UserView.vue";
import UserMessage from "@/views/UserMessage.vue";

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/',component: InfoView},
    { path: '/info', component: InfoView },
    { path: '/user',component:UserView},
    { path: '/usermessage',component:UserMessage},
    { path: '/announcement', component: AnnounceView },
    { path: '/login', component: LoginView },
    { path: '/guide', component: GuideView },
    { path: '*', redirect: '/InfoView' } // 默认重定向到信息展示页面
  ],
  mode: 'history'
});
