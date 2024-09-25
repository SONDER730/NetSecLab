<template>
<el-row class="tac">
  <el-col :span="100">
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

          <!-- 根据角色显示两个个人主页的 item -->
          <el-menu-item v-if="userRole === 'student'" index="/studentInfo">
            <router-link to="/studentInfo" class="custom-router-link">个人信息</router-link>
          </el-menu-item>
          <el-menu-item v-else-if="userRole === 'teacher'" index="/teacherInfo">
            <router-link to="/teacherInfo" class="custom-router-link">个人信息</router-link>
          </el-menu-item>
          <el-menu-item v-if="userRole === 'student'" index="/student">
            <router-link to="/student" class="custom-router-link">个人应用</router-link>
          </el-menu-item>
          <el-menu-item v-else-if="userRole === 'teacher'" index="/teacher">
            <router-link to="/teacher" class="custom-router-link">个人应用</router-link>
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
    props: ['isLoggedIn', 'userRole'],
      watch: {
      // 监听 isLoggedIn 和 userRole 的变化，并调用更新方法
        isLoggedIn(newVal) {
          this.updateMenu();
        },
        userRole(newVal) {
          this.updateMenu();
      }
      },
    methods: {

      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      updateMenu() {
      // 当 isLoggedIn 或 userRole 发生变化时自动重新渲染
      console.log('更新导航栏，当前登录状态:', this.isLoggedIn, '当前角色:', this.userRole);
    },
    }
  }
</script>

<style scoped>

/* 标题样式 */
.sidebar-title {
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
