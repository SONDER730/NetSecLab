<template>
  <div id="home" class="container">
    <!-- 左侧导航栏 -->
    <aside class="sidebar">
      <ul>
        <li>
          <!-- 信息展示 - 可以展开子菜单 -->
          <div @click="toggleInfoDisplay" class="menu-title">
            信息展示
          </div>
          <ul v-if="showInfoDisplay" class="submenu">
            <li><router-link to="/Lab">实验室介绍</router-link></li>
            <li><router-link to="/other-info">其他信息</router-link></li>
            <!-- 可以根据需要添加更多选项 -->
          </ul>
        </li>
        <li>
          <!-- 竞赛公示 -->
          <router-link to="/competitions">竞赛公示</router-link>
        </li>
        <li v-if="!loggedIn">
          <!-- 登录 -->
          <router-link to="/login">登录</router-link>
        </li>
        <li v-if="loggedIn">
          <!-- 登录后显示个人账户 -->
          <router-link to="/account">个人账户</router-link>
        </li>
        <li>
          <!-- 使用指南 -->
          <router-link to="/guide">使用指南</router-link>
        </li>
      </ul>
    </aside>

    <!-- 右侧内容窗口 -->
    <main class="content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      loggedIn: false,          // 登录状态
      showInfoDisplay: false,   // 控制信息展示子菜单的显示与隐藏
    };
  },
  mounted() {
    // 检查用户是否已登录，使用 localStorage 作为示例
    this.loggedIn = !!localStorage.getItem('loggedIn');
  },
  methods: {
    toggleInfoDisplay() {
      this.showInfoDisplay = !this.showInfoDisplay;  // 切换信息展示子菜单的显示与隐藏
    },
    handleLogin() {
      this.loggedIn = true;
      localStorage.setItem('loggedIn', 'true');
    },
    handleLogout() {
      this.loggedIn = false;
      localStorage.removeItem('loggedIn');
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  height: 100vh;
}

/* 左侧导航栏样式 */
.sidebar {
  width: 200px;
  background-color: #f8f8f8;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar li {
  margin-bottom: 10px;
}

.sidebar .menu-title {
  font-weight: bold;
  cursor: pointer;
}

.submenu {
  padding-left: 20px;
}

/* 右侧内容区域样式 */
.content {
  flex: 1;
  padding: 20px;
}
</style>
