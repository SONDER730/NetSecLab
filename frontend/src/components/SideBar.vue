<template>
  <el-row>
    <el-col :span="24">
      <h2 class="title">北京邮电大学</h2>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#f5f7fa"
        text-color="#333"
        active-text-color="#409eff"
      >
       <div class="button-container">
        <el-button type="primary" class="full-width" @click="goTo('Info')">
          信息展示
        </el-button>
        <el-button type="primary" class="full-width" @click="goTo('Announcement')">
          竞赛公示
        </el-button>
        <el-button type="primary" class="full-width" @click="goTo('Login')">
          登录
        </el-button>
        <el-button type="primary" class="full-width" @click="goTo('Guide')">
          使用指南
        </el-button>
      </div>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: false, // 根据需要设置登录状态
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log('Opened:', key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log('Closed:', key, keyPath);
    },
    goTo(page) {
      this.$emit('navigate', page); // 使用路由名称跳转
    },
  },
};
</script>

<style scoped>

.title {
  text-align: center;
  margin-bottom: 20px;
  font-weight: bold;
  color: #409eff;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 10px; /* 按钮间的间隔 */
  margin-top: 20px;
  border: white;
}
</style>
