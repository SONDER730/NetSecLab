<template>
  <div class="guide-view">

      <!-- 左侧菜单 -->
    <el-menu
      class="el-menu-vertical"
      :default-active="activeMenu"
      @select="handleMenuSelect"
      background-color="#001f3f"
      text-color="#fff"
      active-text-color="#409eff"
    >
      <el-menu-item index="signup_com">
        <h2>如何报名</h2>
      </el-menu-item>
      <el-menu-item index="competitions">
        <h2>查看竞赛信息</h2>
      </el-menu-item>
      <el-menu-item index="contact">
        <h2>联系我们</h2>
      </el-menu-item>
    </el-menu>

  <!-- 右侧内容区域 -->
    <div class="content-container">
      <div class="main">
          <h1>使用指南</h1>
      </div>


      <!-- 竞赛报名部分 -->
      <div v-if="activeMenu === 'signup_com'">
        <div>
          <p>这里是竞赛报名的步骤</p>
        </div>
      </div>

       <!-- 查看实验室信息部分 -->
      <div v-if="activeMenu === 'competitions'">
        <div>
          <p>这里是查看竞赛信息的步骤</p>
        </div>
      </div>

      <!-- 联系我们信息部分 -->
      <div v-if="activeMenu === 'contact'">
        <div>
          <p>这里是联系我们的步骤</p>
        </div>
      </div>

    </div>
  </div>
</template>




<script>
export default {
  data(){
    return{
      activeMenu: 'signup_com',
    }
  },
   methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
  },
  name: 'GuideView',
};
</script>

<style scoped>
.guide-view {
  display: flex;
  height: 100vh;
  background-color: #001f3f;
}

/* 左侧菜单样式 */
.el-menu-vertical {
  width: 250px;
  background-color: #001f3f;
  color: #fff;
  text-align: center;
}

.content-container {
  flex: 1;
  padding: 20px;
  background-color: white;
  color: black;
}

h1 {
  font-size: 2rem;
  color: #409EFF;
}

h2{
  font-size:1rem;
  color:white;
}

.el-menu-item:hover {
  background-color: #409eff !important;
}
</style>
