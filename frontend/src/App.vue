<template>
  <div id="app">
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="17%">
        <SideBar :isLoggedIn="isLoggedIn" :userRole="userRole"/>
      </el-aside>

      <!-- 主内容区域 -->
      <el-main>
        <router-view @login="handleLogin"/> <!-- 动态加载内容 -->
      </el-main>
    </el-container>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'; // 导入 SideBar 组件

export default {
  name: 'App',
  components: {
    SideBar, // 注册 SideBar 组件
  },
  data() {
    return {
      isLoggedIn: false, // 根据需要设置登录状态
      userRole: '', // 用户角色（'student' 或 'teacher'）
    };
  },

  methods: {
    handleLogin(role) {
      this.isLoggedIn = true;
      this.userRole = role; // 设置用户身份
      this.$router.push('/info');
    }
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

.el-container {
  height: 100vh; /* 使用视口高度，使容器占满整个屏幕 */
}

.el-aside {
  background-color: white;
  color: #333;
  text-align: center;
  //display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  padding: 20px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  padding: 20px;
}
</style>
