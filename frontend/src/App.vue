<template>
  <div id="app">
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="20%">
        <SideBar />
      </el-aside>

      <!-- 主内容区域 -->
      <el-main>
        <router-view /> <!-- 动态加载内容 -->
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
    };
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
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  margin: 0px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  padding: 20px;
  text-align: center;
  line-height: 160px;
}
</style>
