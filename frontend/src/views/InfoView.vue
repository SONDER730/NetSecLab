<template>
  <div class="info-view">
    <!-- 主内容区域 -->
    <el-container class="content-container">
      <!-- 左侧导航栏 -->
      <el-aside width="20%" class="aside-nav">
        <h3 class="aside-title">实验中心介绍</h3>
        <el-menu
          default-active="4"
          class="el-menu-vertical-demo"
        >
          <el-menu-item index="1">102-103教室</el-menu-item>
          <el-menu-item index="2">104-105教室</el-menu-item>
          <el-menu-item index="3">107-108教室</el-menu-item>
          <el-menu-item index="4">网109-110教室</el-menu-item>
          <el-menu-item index="5">112-113网络靶场</el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 右侧内容展示 -->
      <el-main class="main-content">
        <div class="article-content">
          <h2>网络空间安全学院</h2>
          <p>
            网络空间安全学院是北京邮电大学的重要学术单位之一，专注于网络安全、信息安全、密码技术等多个领域的研究与教学。
            该学院致力于培养具有国际视野的网络安全人才，并积极参与国家和行业的安全技术标准制定工作。
          </p>
          <p>
            主要课程包括：网络攻防技术、密码学原理与应用、网络安全协议分析、区块链技术等。
            学院与多家国内外知名企业和研究机构建立了长期合作关系，提供丰富的实习和科研机会。
          </p>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'InfoView',
};
</script>

<style scoped>
/* 顶层容器样式 */
.info-view {
  font-family: 'Arial', sans-serif;
  background-color: #f2f4f7; /* 背景色 */
}

/* 主内容容器样式 */
.content-container {
  display: flex;
  padding: 20px;
}

/* 侧边栏样式 */
.aside-nav {
  background-color: #ffffff; /* 侧边栏背景色 */
  padding: 20px;
  border-right: 1px solid #dcdcdc; /* 分隔线 */
  box-shadow: 0px 2px 12px rgba(0, 0, 0, 0.05); /* 添加轻微阴影 */
  border-radius: 8px; /* 圆角效果 */
}

.aside-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center; /* 居中对齐标题 */
}

/* 主内容区样式 */
.main-content {
  padding: 40px;
  background-color: white;
  flex: 1;
  box-shadow: 0px 2px 12px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  border-radius: 8px; /* 圆角效果 */
  margin-left: 20px;
}

/* 文章标题样式 */
.article-content h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #409eff; /* 标题颜色 */
}

/* 文章段落样式 */
.article-content p {
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 20px;
  color: #333;
}
</style>
