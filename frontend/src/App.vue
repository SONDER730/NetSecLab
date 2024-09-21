<template>
  <div id="app">
    <!-- 全局导航栏 -->
    <header>
      <nav>
        <router-link to="/Home">首页</router-link> |
        <router-link to="/Competition_Announcement">竞赛公示</router-link> |
        <router-link to="/Guide">使用指南</router-link> |
        <!-- 仅在未登录时显示“登录”链接 -->
        <router-link v-if="!loggedIn" to="/Login">登录</router-link>
        <!-- 仅在已登录时显示“个人账户”链接 -->
        <router-link v-if="loggedIn" to="/account">个人账户</router-link>
      </nav>
    </header>

    <!-- 动态展示不同的页面内容 -->
    <router-view></router-view>

    <!-- 固定内容：竞赛公示和使用指南（登录和未登录都显示） -->
    <section>
      <h2>信息展示</h2>
      <p>这里展示实验中心的最新信息。</p>
    </section>

    <competition-announcement></competition-announcement>
    <guide></guide>
  </div>
</template>

<script>
// 引入固定显示的子组件
import CompetitionAnnouncement from '@/components/CompetitionAnnouncement.vue';
import Guide from '@/components/Guide.vue';

export default {
  name: 'App',
  components: {
    CompetitionAnnouncement,
    Guide,
  },
  data() {
    return {
      loggedIn: false,  // 用户是否已登录
    };
  },
  mounted() {
    // 在组件加载时检查用户的登录状态
    this.checkLoginStatus();
  },
  methods: {
    // 检查用户是否已登录（可以从服务器或 localStorage 获取）
    checkLoginStatus() {
      // 模拟从 localStorage 获取用户登录状态
      this.loggedIn = !!localStorage.getItem('loggedIn');
    },
    handleLogin() {
      // 当用户登录时，设置登录状态
      this.loggedIn = true;
      localStorage.setItem('loggedIn', 'true');  // 将登录状态保存到 localStorage
    },
    handleLogout() {
      // 当用户登出时，清除登录状态
      this.loggedIn = false;
      localStorage.removeItem('loggedIn');  // 清除登录状态
    }
  },
};
</script>

<style scoped>
header {
  background-color: #f0f0f0;
  padding: 10px;
  text-align: center;
}

nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #333;
}

nav a:hover {
  color: #007BFF;
}

section {
  margin: 20px 0;
}

h2 {
  color: #444;
}

p {
  font-size: 1.2rem;
}
</style>
