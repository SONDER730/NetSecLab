<template>
<el-row class="tac">
  <el-col :size="1000">
    <h5 class="sidebar-title">北京邮电大学</h5>
    <el-menu
      default-active="$route.path"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#fff"
      text-color="#333"
      active-text-color="#409EFF"
    >

      <!-- 信息展示 -->
      <el-menu-item index="/info">
        <router-link to="/info" class="custom-router-link">
          <i class="el-icon-menu"></i>
          <span class="nav-text">信息展示</span>
        </router-link>
      </el-menu-item>

    <!-- 竞赛公示 -->
      <el-menu-item index="/announcement">
        <router-link to="/announcement" class="custom-router-link">
          <i class="el-icon-menu"></i>
          <span class="nav-text">竞赛公示</span>
        </router-link>
      </el-menu-item>

    <!-- 登录前显示 登录 -->
      <el-menu-item v-if="!isLoggedIn" index="/login">
        <router-link to="/login" class="custom-router-link">
          <i class="el-icon-user"></i>
          <span class="nav-text">登录</span>
        </router-link>
      </el-menu-item>

        <!-- 个人主页 -->
        <el-submenu v-else index="3" class="no-arrow-submenu">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span class="nav-text">个人主页</span>
          </template>
          <el-menu-item index="/user">
            <router-link to="/user" class="custom-router-link">用户信息</router-link>
          </el-menu-item>
          <el-menu-item index="/usermessage">
            <router-link to="/usermessage" class="custom-router-link">用户通知</router-link>
          </el-menu-item>
        </el-submenu>

        <!-- 使用指南 -->
        <el-menu-item index="/guide">
          <router-link to="/guide" class="custom-router-link">
            <i class="el-icon-setting"></i>
            <span class="nav-text">使用指南</span>
          </router-link>
        </el-menu-item>
    </el-menu>
  </el-col>
</el-row>
</template>

<script>
  export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>
/* 标题样式 */
.sidebar-title {
  display: flex;
  text-align: center;
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 40px;
  font-weight: bold;
}
.custom-router-link {
  text-decoration: none; /* 移除下划线 */
  color: inherit; /* 继承字体颜色 */
  display: flex;
  align-items: center;
}
</style>
