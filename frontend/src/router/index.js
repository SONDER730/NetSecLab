import Vue from 'vue';
import Router from 'vue-router';
import InfoView from '@/views/InfoView.vue';
import AnnounceView from '@/views/AnnounceView.vue';
import LoginView from '@/views/LoginView.vue';
import GuideView from '@/views/GuideView.vue';
import StuView from "@/views/StuView.vue";
import TeacherView from "@/views/TeacherView.vue";
import Profile  from "@/components/Profile.vue";
import StuProfile from "@/views/StuProfile.vue";
import TeaProfile from "@/views/TeaProfile.vue";
Vue.use(Router);

export default new Router({
  routes: [
    { path: '/',redirect:'/info'},
    { path: '/info', component: InfoView },
    { path: '/studentInfo',component:StuProfile},
    { path: '/teacherInfo',component:TeaProfile},
    { path: '/student',component:StuView},
    { path: '/teacher',component:TeacherView},
    { path: '/Profile',component:Profile},
    { path: '/announcement', component: AnnounceView },
    { path: '/login', component: LoginView },
    { path: '/guide', component: GuideView },
    { path: '*', redirect: '/InfoView' } // 默认重定向到信息展示页面
  ],
  mode: 'history'
});
