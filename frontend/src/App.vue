<template>
  <div id="app">
    <div class="container">
      <!-- 左侧导航栏 -->
      <div class="sidebar">
        <SideBar @navigate="goTo" />
      </div>

      <div class="main-container">
        <!-- 右侧内容区域 -->
        <el-header class="header">
          <h2>网站标题</h2>
        </el-header>

        <el-main class="main">
          <router-view></router-view> <!-- 动态加载内容 -->
        </el-main>

        <el-footer class="footer">
          <span>底部信息 © 2024</span>
        </el-footer>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'; // 确保路径正确

export default {
  components: {
    SideBar, // 注册 SideBar 组件
  },
  data() {
    return {
      isLoggedIn: false, // 根据需要设置登录状态
    };
  },
  methods: {
    goTo(page) {
      this.$router.push({ name: page }); // 执行路由跳转
    },
  },
};
</script>

<style>
html, body {
  margin: 0;
  height: 100%;
}

#app {
  height: 100%;
}

.container {
  display: flex;
  height: 100%;
}

.sidebar {
  background-color: #fff;
  border-right: 1px solid #e4e4e4;
  height: 100%;
  padding: 20px;
}

.main-container {
  margin: 10px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.header {
  background-color: #409eff;
  color: white;
  text-align: center;
  padding: 15px;
}

.main {
  flex: 1;
  padding: 20px;
}

.footer {
  background-color: #f5f7fa;
  text-align: center;
  padding: 10px;
}
</style>
