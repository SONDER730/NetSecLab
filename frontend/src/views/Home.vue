<template>
  <div>
    <!-- 这是根元素，包裹所有内容 -->
    <div class="home-container">
      <!-- 第一个div：欢迎界面 -->
      <section class="welcome-section">
        <div class="welcome-text">
          <h1>欢迎来到北京邮电大学网络空间安全实验平台</h1>
          <p>我们致力于为网络空间安全的研究和实践提供坚实的技术支持，培养卓越的网络安全人才。</p>
        </div>
      </section>

      <!-- 第二个div：实验室滚动图片 -->
      <section class="lab-carousel-section">
        <h2>实验室展示</h2>
        <!-- 轮播图展示图片 -->
        <el-carousel :interval="4000" type="card" height="300px">
          <el-carousel-item v-for="(image, index) in carouselImages" :key="index">
            <img :src="image" alt="实验室展示图片" class="carousel-image" />
          </el-carousel-item>
        </el-carousel>
      </section>

      <!-- 第三个div：特征介绍 -->
      <section class="features-section">
        <h2 class="feature-black">我们的特色</h2>
        <div class="features-container">
          <div class="feature">
            <h3>高质量实验设备</h3>
            <p>我们拥有最先进的实验设施，确保学生能够在真实的环境中进行实验操作。</p>
          </div>
          <div class="feature">
            <h3>行业合作</h3>
            <p>与多个知名企业合作，提供丰富的实习机会和实际项目训练。</p>
          </div>
          <div class="feature">
            <h3>顶级师资力量</h3>
            <p>由国内外知名教授和专家组成的师资团队，提供专业的指导与支持。</p>
          </div>
        </div>
        <div class="features-container">
          <div class="feature">
            <h3>高质量实验设备</h3>
            <p>我们拥有最先进的实验设施，确保学生能够在真实的环境中进行实验操作。</p>
          </div>
          <div class="feature">
            <h3>行业合作</h3>
            <p>与多个知名企业合作，提供丰富的实习机会和实际项目训练。</p>
          </div>
          <div class="feature">
            <h3>顶级师资力量</h3>
            <p>由国内外知名教授和专家组成的师资团队，提供专业的指导与支持。</p>
          </div>
        </div>
      </section>

      <!-- 第四个div：竞赛公示 -->
      <section class="competition-section">
        <div class="competition-text">
          <!-- 第一部分：竞赛介绍 -->
          <div class="competition-intro">
            <h2>网安竞赛</h2>
            <p>网络安全竞赛是提升学生技能与知识的绝佳平台。通过参与竞赛，学生能够接触到最前沿的技术，并挑战自我。</p>
          </div>

          <!-- 第二部分：平台介绍 -->
          <div class="competition-platform">
            <h3>竞赛公示平台</h3>
            <p>在我们的竞赛公示平台上，您可以了解到最新的竞赛信息，查看比赛规则、报名方式、奖项设置等。</p>
          </div>

          <!-- 第三部分：跳转链接 -->
          <div class="competition-links">
            <h4>相关链接</h4>
            <el-button type="primary" class="competition-btn" @click="navigateToPlatform">
              前往竞赛公示平台
            </el-button>
            <el-button type="success" class="competition-btn" @click="navigateToApply">
              申报竞赛
            </el-button>
          </div>
        </div>

        <!-- 右侧图片部分 -->
        <div class="competition-image">
          <img src="@/assets/f-pic3.png" alt="Competition" />
        </div>
      </section>
    </div>

    <!-- 页脚 -->
    <section class="home-footer">
      <div>
        <p>© 2024 北京邮电大学网络空间安全实验平台. 版权所有.</p>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  name: "Home",
  data() {
    return {
      // 实验室滚动展示图片路径
      carouselImages: [
        require('@/assets/banner1.png'),
        require('@/assets/banner7.jpg'),
        require('@/assets/banner8.jpg'),
        // 可以继续添加更多图片路径
      ],
    };
  },
  methods: {
  // 导航到竞赛公示平台
  navigateToPlatform() {
    this.$route.push("/announcement")
  // window.open("https://example.com/competition-platform", "_blank");
  },
  // 导航到竞赛申报页面
  navigateToApply() {
    this.$route.push("/info")
  // window.open("https://example.com/competition-apply", "_blank");
  },
},
};
</script>

<style scoped>
.home-container {
  font-family: 'Arial', sans-serif;
  background-color: #001f3f;
  color: white;
  overflow: hidden;
  padding: 0;
}

/* 第一个div 样式 */
.welcome-section {
  padding: 100px 20px;
  text-align: center;
  background-color: #001f3f;
}

.welcome-text h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.welcome-text p {
  font-size: 1.2rem;
}

/* 第二个div 样式 */
.lab-carousel-section {
  padding: 50px 20px;
  background: linear-gradient(to bottom, #001f3f, #ffffff);;
  text-align: center;
}

.lab-carousel-section h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.carousel-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

/* 第三个div 样式 */
.features-section {
  padding: 50px 20px;
  background-color: white;
}
.feature-black{
  color: black;
}
.features-section h2 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 20px;
}

.features-container {
  display: flex;
  justify-content: space-around;
  margin-bottom: 40px;
  margin-top: 40px;
}

.feature {
  width: 20%;
  background-color: #2C303B;
  padding: 20px;
  border-radius: 8px;
}

.feature h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.feature p {
  font-size: 1rem;
}
/* 第四个div 样式 */

.competition-section {
  margin: 0 auto;
  width: 80%;
  display: flex;
  justify-content: space-between;
  padding: 50px 20px;
  background-color: #001f3f;
  border-top: 1px solid white;
  color: white;
}

.competition-text {
  width: 50%;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.competition-intro h2 {
  font-size: 1.8rem;
  margin-bottom: 15px;
}

.competition-intro p {
  font-size: 1rem;
  line-height: 1.6;
}

.competition-platform h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.competition-platform p {
  font-size: 1rem;
  line-height: 1.6;
}

.competition-links h4 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.competition-btn {
  margin-right: 10px;
}

.competition-image {
  width: 50%;

}

.competition-image img {
  max-width: 100%;
  border-radius: 8px;
}
/* 页脚样式 */
.home-footer {
  padding: 20px 0;
  text-align: center;
  background-color: #001f3f;
  border-top: 1px solid white;
  color: #ccc;
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}
</style>




