<template>
  <div id="app">
    <el-container>
      <!-- 顶部导航栏 -->
<<<<<<< HEAD
      <!-- <el-header> -->
        <SideBar :isLoggedIn="isLoggedIn" :userRole="userRole" @logout="handleLogout"/>
      <!-- </el-header> -->

      <!-- 主内容区域 -->
      <el-main :class="{noneNavbar:$route.path !=='/'}">
=======
      <el-header>
        <SideBar :isLoggedIn="isLoggedIn" :userRole="userRole" @logout="handleLogout"/>
      </el-header>

      <!-- 主内容区域 -->
      <el-main>
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
        <router-view @login="handleLogin" /> <!-- 动态加载内容 -->
      </el-main>
    </el-container>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'; // 导入 SideBar 组件

export default {
  name: 'App',
  components: {
    SideBar,
  },
  data() {
    return {
      isLoggedIn: false,
      userRole: '',
    };
  },
  watch: {
    isLoggedIn(newVal) {
      if (newVal) {
        console.log('用户已登录');
      } else {
        console.log('用户已登出');
      }
    },
    userRole(newVal) {
      if (newVal) {
        console.log(`用户角色为: ${newVal}`);
      }
    },
  },
  methods: {
    handleLogin(role, isLogin) {
      this.isLoggedIn = isLogin; // 更新登录状态
      this.userRole = role; // 更新用户角色
    },
    handleLogout() {
      this.isLoggedIn = false;
      this.userRole = '';
      this.$router.push('/login'); // 跳转到登录页
    },
  },
};
</script>

<style>
<<<<<<< HEAD
.noneNavbar{
  margin-top: 80px !important;
}
=======
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
body, html {
  margin: 0;
  padding: 0;
}

.navbar {
  margin-bottom: 0;
}

.home-container {
  margin-top: 0;
  padding-top: 0;
}

#app {
  height: 100%;
}

.el-container {
<<<<<<< HEAD
  /* //height: 100vh; 使用视口高度，使容器占满整个屏幕 */
=======
  //height: 100vh; /* 使用视口高度，使容器占满整个屏幕 */
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
}

.el-main {
  display: block;
  flex: 1;
  flex-basis: auto;
  overflow: hidden; /* 隐藏溢出部分 */
  box-sizing: border-box;
  background-color: #E9EEF3;
<<<<<<< HEAD
  /* //color: #333; */
=======
  //color: #333;
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
  padding: 0px !important;/* 去掉 padding */
  margin: 0;  /* 去掉 margin */
}
</style>
