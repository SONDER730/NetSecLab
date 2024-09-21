import Vue from 'vue';
import Router from 'vue-router';

// 引入各个页面组件
import Home from '@/views/Home.vue';
import Login from '@/components/Login.vue';
import Guide from '@/components/Guide.vue';
import Competition_Announcement from '@/components/Competition_Announcement.vue';
import Teacher_Dashboard from '@/components/Teacher_Dashboard.vue';
import Student_Dashboard from '@/components/Student_Dashboard.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/login', name: 'Login', component: Login },
    { path: '/guide', name: 'Guide', component: Guide },
    { path: '/competitions', name: 'Competition_Announcement', component: Competition_Announcement },
    { path: '/teacher-dashboard', name: 'Teacher_Dashboard', component: Teacher_Dashboard },
    { path: '/student-dashboard', name: 'Student_Dashboard', component: Student_Dashboard },
    { path: '*', redirect: '/' }  // 重定向未知路径到首页
  ]
});
